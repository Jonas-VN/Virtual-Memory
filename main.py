from Controller import Controller
from functions import parse_data
import PySimpleGUI as Sg


def to_physical(virtual_address, process_id, controller):
    virtual_page_number = virtual_address // 4096
    offset = virtual_address % 4096

    physical_page_number = controller.processes[process_id].get_page_table()[virtual_page_number].get_page_number()
    return physical_page_number + offset


def main():
    instructions = parse_data("instructions_30_3.xml")
    controller = Controller(instructions)

    layout = [[Sg.Text("Besturingssystemen")]], [Sg.Button("Run 1")], [Sg.Button("Run all")]
    window = Sg.Window("Demo", layout)
    Sg.set_options(debug_win_size=(150, 50))
    print = Sg.Print

    while True:
        event, values = window.read()
        if event == "Run 1":
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                controller.one_instruction()

            print(f"\nJiffy: {jiffy}", font="Courier 10 bold")
            print(f"\nPhysical address: {physical_address}", font="Courier 10 bold")

            print("\nCurrent instruction:", font="Courier 10 bold")
            print(current_instruction, font="Courier 10 italic")

            print("\nNext instruction:", font="Courier 10 bold")
            print(next_instruction, font="Courier 10 italic")

            print("\nPage table:", font="Courier 10 bold")
            print(page_tabel, font="Courier 10 italic")

            print("\nRam:", font="Courier 10 bold")
            print(ram, font="Courier 10 italic")
            print()
            print(page_in)
            print(page_out)

        elif event == "Run all":
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_faults = \
                controller.all_instructions()

            print(f"\nJiffy: {jiffy}", font="Courier 10 bold")
            print(f"\nPhysical address: {physical_address}", font="Courier 10 bold")

            print("\nCurrent instruction:", font="Courier 10 bold")
            print(current_instruction, font="Courier 10 italic")

            print("\nNext instruction:", font="Courier 10 bold")
            print(next_instruction, font="Courier 10 italic")

            print("\nPage table:", font="Courier 10 bold")
            print(page_tabel, font="Courier 10 italic")

            print("\nRam:", font="Courier 10 bold")
            print(ram, font="Courier 10 italic")

        elif event == Sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()

