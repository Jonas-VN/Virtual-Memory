from Controller import Controller
from functions import parse_data


def main():
    instructions = parse_data("instructions_20000_20.xml")
    controller = Controller(instructions)
    jiffy, instruction, page_table, ram = controller.one_instruction()
    print("Jiffy:", jiffy)
    print("Instruction:", instruction)
    for page in page_table:
        print(page)
    for ram_page in ram:
        print(ram_page)
    print('-----------------------------------------------------')

    for _ in range(1500):
        jiffy, instruction, page_table, ram = controller.one_instruction()

    jiffy, instruction, page_table, ram = controller.one_instruction()
    print("Jiffy:", jiffy)
    print("Instruction:", instruction)
    for page in page_table:
        print(page)
    for ram_page in ram:
        print(ram_page)
    print('-----------------------------------------------------')


if __name__ == "__main__":
    main()
