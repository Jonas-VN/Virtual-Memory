from Frame import Frame
from Process import Process
from Instruction import Instruction
import xml.etree.ElementTree as Et
from tabulate import tabulate


class Program:
    def __init__(self, file):
        self.instructions = self.load_instructions(file)
        self.jiffy = 0
        self.ram = [Frame(i) for i in range(12)]
        self.processes = []
        self.processes_in_ram = []

    @staticmethod
    def load_instructions(filename):
        tree = Et.parse("./Data/" + filename)
        root = tree.getroot()
        instructions = []
        for instruction in root:
            instructions.append(
                Instruction(int(instruction[0].text), instruction[1].text, int(instruction[2].text)))
        return instructions

    @staticmethod
    def get_lru_frame(frames):
        lru_frame = None
        for frame in frames:
            if lru_frame is None:
                lru_frame = frame
                if frame.get_page() is None:
                    break
            if frame.get_page() is None:
                lru_frame = frame
                break
            if frame.get_page().get_last_access_time() < lru_frame.get_page().get_last_access_time():
                lru_frame = frame
        return lru_frame

    def get_process(self, instruction):
        return self.processes[instruction.get_process_id()]

    def get_frame_from_ram(self, process_id):
        frames = []
        for frame in self.ram:
            if frame.get_process_id() == process_id:
                frames.append(frame)
        return frames

    def start(self, instruction):
        process = Process(instruction.get_process_id())
        self.processes.append(process)

        if not self.processes_in_ram:
            # Empty RAM
            for frame in self.ram:
                frame.set_process_id(self.processes[0].get_process_id())
                frame.set_page(None)
            self.processes_in_ram.append(instruction.get_process_id())

        else:
            # RAM is not empty
            old_frames_per_process = 12 // len(self.processes_in_ram)
            new_frames_per_process = 12 // (len(self.processes_in_ram) + 1)
            frames_to_remove_per_process = old_frames_per_process - new_frames_per_process

            # Nodige frames van andere processen verwijderen en al op het juiste process id zetten
            for process_id in self.processes_in_ram:
                frames_in_ram = self.get_frame_from_ram(process_id)
                for i in range(frames_to_remove_per_process):
                    lru_frame = self.get_lru_frame(frames_in_ram)
                    if lru_frame.get_page():  # and lru_frame.get_page().get_present_bit(): -> overbodig, als niet present is page None
                        self.processes[process_id].increment_page_out()

                    frames_in_ram.remove(lru_frame)
                    lru_frame.set_process_id(instruction.get_process_id())
                    lru_frame.set_page(None)

            self.processes_in_ram.append(instruction.get_process_id())

    def write(self, instruction):
        self.read(instruction)
        self.get_process(instruction).set_modified_bit(instruction.get_address())

    def read(self, instruction):
        process_id = instruction.get_process_id()
        process = self.processes[process_id]
        address = instruction.get_address()
        page = process.get_page(address)

        if not page.get_present_bit():
            frames_in_ram = self.get_frame_from_ram(process_id)
            lru_frame = self.get_lru_frame(frames_in_ram)

            # LRU verwijderen
            if lru_frame.get_page():
                frame_page = lru_frame.get_page()
                frame_page.clear_page()
                process.increment_page_out()

            # Nieuw frame toevoegen
            lru_frame.set_page(page)
            page.set_page(lru_frame.get_frame_number())
            process.increment_page_in()

        page.set_last_access_time(self.jiffy)

    def terminate(self, instruction):
        # Nog maar 1 process in de ram, alles opruimen
        if len(self.processes_in_ram) == 1:
            for frame in self.ram:
                if frame.get_page():
                    frame.get_page().clear_page()
                    frame.set_page(None)
                    self.processes[self.processes_in_ram[0]].increment_page_out()
                frame.set_process_id(None)

            self.processes_in_ram.remove(instruction.get_process_id())

        # Nodige processen extra ruimte geven
        else:
            old_frames_per_process = 12 // len(self.processes_in_ram)
            new_frames_per_process = 12 // (len(self.processes_in_ram) - 1)
            frames_to_add_per_process = new_frames_per_process - old_frames_per_process

            self.processes_in_ram.remove(instruction.get_process_id())

            frames_in_ram = self.get_frame_from_ram(instruction.get_process_id())
            for process_id in self.processes_in_ram:
                for i in range(frames_to_add_per_process):
                    # Nog pages in RAM van dat process
                    if frames_in_ram[0].get_page():
                        self.processes[process_id].increment_page_out()
                    frames_in_ram[0].set_process_id(process_id)
                    frames_in_ram[0].set_page(None)
                    frames_in_ram.remove(frames_in_ram[0])
        self.get_process(instruction).clear_page_table()

    def run_instruction(self, instruction):
        if instruction.get_operation() == "Start":
            self.start(instruction)
        elif instruction.get_operation() == "Write":
            self.write(instruction)
        elif instruction.get_operation() == "Read":
            self.read(instruction)
        elif instruction.get_operation() == "Terminate":
            self.terminate(instruction)
        self.jiffy += 1

    def run_one(self):
        if self.jiffy < len(self.instructions):
            instruction = self.instructions[self.jiffy]
            self.run_instruction(instruction)

            return_values = [self.jiffy]

            virtual_page_number = instruction.get_address() // 4096
            offset = instruction.get_address() % 4096
            physical_page_number = self.get_process(instruction).get_page_table()[virtual_page_number].get_frame_number()
            if physical_page_number is not None:
                physical_address = physical_page_number * 4096 + offset
            else:
                physical_address = 0
            return_values.append(physical_address)

            return_values.append(instruction)

            if self.jiffy < len(self.instructions):
                return_values.append(self.instructions[self.jiffy])  # Jiffy is al geïncrementeerd, dus wijst al naar de volgende instructie
            else:
                return_values.append("/")

            page_numbers = ["Page Number"]
            present_bits = ["Present Bit"]
            modified_bits = ["Modified Bit"]
            last_access_times = ["Last Access Time"]
            frame_numbers = ["Frame Number"]
            for page in self.get_process(instruction).get_page_table():
                page_numbers.append(page.get_page_number())
                present_bits.append(page.get_present_bit())
                modified_bits.append(page.get_modified_bit())
                last_access_times.append(page.get_last_access_time())
                frame_numbers.append(page.get_frame_number())
            table = [page_numbers, present_bits, modified_bits, last_access_times, frame_numbers]
            return_values.append(tabulate(table, tablefmt="grid"))

            process_ids = ["Process ID"]
            page_numbers = ["Page Number"]
            frame_numbers = ["Frame Number"]
            for frame in self.ram:
                process_ids.append(frame.get_process_id())
                if frame.get_page():
                    page_numbers.append(frame.get_page().get_page_number())
                else:
                    page_numbers.append("")
                frame_numbers.append(frame.get_frame_number())
            table = [frame_numbers, process_ids, page_numbers]
            return_values.append(tabulate(table, tablefmt="grid"))

            page_in = 0
            page_out = 0
            for process in self.processes:
                page_in += process.get_page_in()
                page_out += process.get_page_out()

            return_values.append(page_in)
            return_values.append(page_out)

            return return_values

    def run_all(self):
        while self.jiffy < len(self.instructions) - 1:
            self.run_instruction(self.instructions[self.jiffy])
        return self.run_one()
