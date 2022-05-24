from Program import Program
import PySimpleGUI as Sg


def main():
    program = None
    reached_end = False
    file_selected = False

    button_menu_def = ['File', ['instructions_30_3.xml', 'instructions_20000_4.xml', 'instructions_20000_20.xml']]

    layout = [[Sg.Text("Besturingssystemen")]], \
             [Sg.ButtonMenu('Choose your file', menu_def=button_menu_def, key='files')], \
             [Sg.Button("Run 1")], [Sg.Button("Run all")], [Sg.Button("Reset")]

    window = Sg.Window("Demo", layout, grab_anywhere=True, keep_on_top=True)
    Sg.set_options(debug_win_size=(150, 50))
    debug = Sg.Print

    while True:
        event, values = window.read()
        if file_selected:
            values = {"files": None}

        if (event == "Run 1" or event == "Run all") and file_selected and reached_end:
            debug("You can't do that, reset first.")

        if event == "Run 1" and not reached_end and program:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                program.run_one()

            debug(background_color="black")

            debug(f"\nJiffy: {jiffy}", font="Courier 10 bold")
            debug(f"\nPhysical address: {physical_address}", font="Courier 10 bold")
            debug(f"Physical page: {physical_address // 4096}", font="Courier 10 bold")

            debug("\nCurrent instruction:", font="Courier 10 bold")
            debug(current_instruction, font="Courier 10 italic")

            debug("\nNext instruction:", font="Courier 10 bold")
            debug(next_instruction, font="Courier 10 italic")

            debug("\nPage table:", font="Courier 10 bold")
            debug(page_tabel, font="Courier 10 italic")

            debug("\nRam:", font="Courier 10 bold")
            debug(ram, font="Courier 10 italic")

            debug(f"\nPage in: {page_in}", font="Courier 10 bold")
            debug(f"Page out: {page_out}\n", font="Courier 10 bold")

            debug(background_color="black")

            if next_instruction == "/":
                debug("\n\nEnd of the program.\n\n", font="Courier 15 bold")
                reached_end = True

        elif event == "Run all" and not reached_end and program:
            jiffy, physical_address, current_instruction, next_instruction, page_tabel, ram, page_in, page_out = \
                program.run_all()

            debug(background_color="black")

            debug(f"\nJiffy: {jiffy}", font="Courier 10 bold")
            debug(f"\nPhysical address: {physical_address}", font="Courier 10 bold")

            debug("\nCurrent instruction:", font="Courier 10 bold")
            debug(current_instruction, font="Courier 10 italic")

            debug("\nNext instruction:", font="Courier 10 bold")
            debug(next_instruction, font="Courier 10 italic")

            debug("\nPage table:", font="Courier 10 bold")
            debug(page_tabel, font="Courier 10 italic")

            debug("\nRam:", font="Courier 10 bold")
            debug(ram, font="Courier 10 italic")

            debug(f"\nPage in: {page_in}", font="Courier 10 bold")
            debug(f"Page out: {page_out}\n", font="Courier 10 bold")

            debug(background_color="black")

            if next_instruction == "/":
                debug("\n\nEnd of the program.\n\n", font="Courier 15 bold")
                reached_end = True

        elif event == "Reset":
            program = None
            file_selected = False
            Sg.easy_print_close()

        elif values["files"] == "instructions_30_3.xml":
            file_selected = True
            debug(background_color="black")
            program = Program("instructions_30_3.xml")
            reached_end = False
            debug("\n30 instructions with 3 processes\n", font="Courier 15 bold")
            debug(background_color="black")

        elif values["files"] == "instructions_20000_4.xml":
            file_selected = True
            debug(background_color="black")
            program = Program("instructions_20000_4.xml")
            reached_end = False
            debug("\n20.000 instructions with 4 processes\n", font="Courier 15 bold")
            debug(background_color="black")

        elif values["files"] == "instructions_20000_20.xml":
            file_selected = True
            debug(background_color="black")
            program = Program("instructions_20000_20.xml")
            reached_end = False
            debug("\n20.000 instructions with 20 processes\n", font="Courier 15 bold")
            debug(background_color="black")

        elif event == Sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
