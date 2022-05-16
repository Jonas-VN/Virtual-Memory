from Controller import Controller
from functions import parse_data
import PySimpleGUI as Sg


def main():
    instructions = parse_data("instructions_20000_4.xml")
    controller = Controller(instructions)
    reached_end = False

    layout = [[Sg.Text("Besturingssystemen")]], [Sg.Button("Run 1")], [Sg.Button("Run all")]
    window = Sg.Window("Demo", layout)
    Sg.set_options(debug_win_size=(150, 50))
    print = Sg.Print

    while True:
        event, values = window.read()
        if event == "Run 1" and not reached_end:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                controller.one_instruction()

            print(background_color="black")

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

            print(f"\nPage in: {page_in}", font="Courier 10 bold")
            print(f"Page out: {page_out}\n", font="Courier 10 bold")

            print(background_color="black")

            if next_instruction == "/":
                print("\n\nEnd of the program.", font="Courier 15 bold")
                reached_end = True

        elif event == "Run all" and not reached_end:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                controller.all_instructions()

            print(background_color="black")

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

            print(f"\nPage in: {page_in}", font="Courier 10 bold")
            print(f"Page out: {page_out}\n", font="Courier 10 bold")

            print(background_color="black")

            if next_instruction == "/":
                print("\n\nEnd of the program.", font="Courier 15 bold")
                reached_end = True

        elif event == Sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()

