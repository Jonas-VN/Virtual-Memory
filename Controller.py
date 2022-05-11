from Frame import Frame
from Process import Process


class Controller:
    def __init__(self, instructions):
        self.instructions = instructions
        self.jiffy = 0
        self.ram = []
        self.processes = []
        self.processes_in_ram = []

        for i in range(12):
            self.ram.append(Frame(i))

    def get_ram(self):
        return self.ram

    def get_processes_in_ram(self):
        return self.processes_in_ram

    def get_jiffy(self):
        return self.jiffy

    def get_instructions(self):
        return self.instructions

    def get_processes(self):
        return self.processes

    @staticmethod
    def get_lru_frame(frames):
        lru_frame = None
        for frame in frames:
            if lru_frame is None:
                lru_frame = frame
                if frame.get_page() is None:
                    break
                continue
            if frame.get_page() is None:
                lru_frame = frame
                break
            if frame.get_page().get_last_access_time() < lru_frame.get_page().get_last_access_time():
                lru_frame = frame
        return lru_frame

    def get_frames_in_ram_with_process_id(self, process_id):
        frames = []
        for frame in self.ram:
            if frame.get_process_id() == process_id:
                frames.append(frame)
        return frames

    def check_ram(self, instruction):
        process_id = instruction.get_process_id()
        process = self.processes[process_id]
        address = instruction.get_address()
        page = process.get_page(address)

        if not page.get_present_bit():
            frames_in_ram_with_process_id = self.get_frames_in_ram_with_process_id(process_id)
            lru_frame = self.get_lru_frame(frames_in_ram_with_process_id)
            if lru_frame.get_page():
                frame_page = lru_frame.get_page()
                frame_page.clear_page()

            lru_frame.set_page(page)
            page.set_page(lru_frame.get_frame_number())
            process.increment_page_faults()

        page.set_last_access_time(self.jiffy)

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

            available_frames = []
            for process_id in self.processes_in_ram:
                frames_in_ram_with_process_id = self.get_frames_in_ram_with_process_id(process_id)
                for i in range(frames_to_remove_per_process):
                    lru_frame = self.get_lru_frame(frames_in_ram_with_process_id)
                    available_frames.append(lru_frame)
                    frames_in_ram_with_process_id.remove(lru_frame)

            for frame in available_frames:
                frame.set_process_id(instruction.get_process_id())
                frame.set_page(None)

            self.processes_in_ram.append(instruction.get_process_id())

    def write(self, instruction):
        self.check_ram(instruction)
        self.processes[instruction.get_process_id()].write(instruction.get_address())

    def read(self, instruction):
        self.check_ram(instruction)

    def terminate(self, instruction):
        if len(self.processes_in_ram) == 1:
            for frame in self.ram:
                if frame.get_page():
                    frame.get_page().clear_page()
                    frame.set_page(None)
                frame.set_process_id(-1)

            self.processes_in_ram.remove(instruction.get_process_id())

        else:
            old_frames_per_process = 12 // len(self.processes_in_ram)
            new_frames_per_process = 12 // (len(self.processes_in_ram) - 1)
            frames_to_add_per_process = new_frames_per_process - old_frames_per_process

            self.processes_in_ram.remove(instruction.get_process_id())

            frames_in_ram_with_process_id = self.get_frames_in_ram_with_process_id(instruction.get_process_id())
            for process_id in self.processes_in_ram:
                for i in range(frames_to_add_per_process):
                    frames_in_ram_with_process_id[0].set_process_id(process_id)
                    frames_in_ram_with_process_id[0].set_page(None)
                    frames_in_ram_with_process_id.remove(frames_in_ram_with_process_id[0])

    def select_instruction(self, instruction):
        if instruction.get_operation() == "Start":
            self.start(instruction)
        elif instruction.get_operation() == "Write":
            self.write(instruction)
        elif instruction.get_operation() == "Read":
            self.read(instruction)
        elif instruction.get_operation() == "Terminate":
            self.terminate(instruction)
        self.jiffy += 1

    def one_instruction(self):
        if self.jiffy < len(self.instructions):
            instruction = self.instructions[self.jiffy]
            self.select_instruction(instruction)

            return_values = []
            return_values.append(self.jiffy)  # Jiffy
            return_values.append(instruction)  # Instruction
            return_values.append(self.processes[instruction.get_process_id()].get_page_table())  # Page table
            return_values.append(self.ram)  # RAM
            return return_values




    def all_instructions(self):
        while self.jiffy < len(self.instructions):
            self.select_instruction(self.instructions[self.jiffy])
