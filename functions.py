import xml.etree.ElementTree as Et
from Instruction import Instruction


def parse_data(filename):
    tree = Et.parse("./Data/" + filename)
    root = tree.getroot()
    instructions = []

    for instruction in root:
        instructions.append(Instruction(int(instruction[0].text), instruction[1].text, int(instruction[2].text)))
    return instructions
