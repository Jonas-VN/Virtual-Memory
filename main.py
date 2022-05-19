from Program import Program
import PySimpleGUI as Sg


def main():
    program = None
    reached_end = False

    layout = [[Sg.Text("Besturingssystemen")]], \
             [Sg.Button("Run 1")], [Sg.Button("Run all")], \
             [Sg.Button("30_3")], [Sg.Button("20000_4")], [Sg.Button("20000_20")]
    window = Sg.Window("Demo", layout, grab_anywhere=True, keep_on_top=True)
    Sg.set_options(debug_win_size=(150, 50))
    print = Sg.Print

    while True:
        event, values = window.read()
        if event == "Run 1" and not reached_end and program:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                program.run_one()

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
                print("\n\nEnd of the program.\n\n", font="Courier 15 bold")
                reached_end = True

        elif event == "Run all" and not reached_end and program:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                program.run_all()

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
                print("\n\nEnd of the program.\n\n", font="Courier 15 bold")
                reached_end = True

        elif event == "30_3":
            Sg.easy_print_close()
            print(background_color="black")
            program = Program("instructions_30_3.xml")
            reached_end = False
            print("\n30 instructions with 3 processes\n", font="Courier 15 bold")
            print(background_color="black")

        elif event == "20000_4":
            Sg.easy_print_close()
            print(background_color="black")
            program = Program("instructions_20000_4.xml")
            reached_end = False
            print("\n20.000 instructions with 4 processes\n", font="Courier 15 bold")
            print(background_color="black")

        elif event == "20000_20":
            Sg.easy_print_close()
            print(background_color="black")
            program = Program("instructions_20000_20.xml")
            reached_end = False
            print("\n20.000 instructions with 20 processes\n", font="Courier 15 bold")
            print(background_color="black")

        elif event == Sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()

