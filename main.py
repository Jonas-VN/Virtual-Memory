from Controller import Controller
from functions import parse_data
import PySimpleGUI as Sg


def main():
    instructions = parse_data("instructions_20000_20.xml")
    controller = Controller(instructions)

    layout = [[Sg.Text("Besturingssystemen")]], [Sg.Button("Run 1")], [Sg.Button("Run all")]
    window = Sg.Window("Demo", layout)
    while True:
        event, values = window.read()
        if event == "Run 1":
            Sg.Print(controller.one_instruction())
        elif event == "Run all":
            print("alle processen")
        elif event == Sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()

