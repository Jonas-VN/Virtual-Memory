import xml.etree.ElementTree as ET


def parse_data(filename):
    tree = ET.parse("./Data/" + filename)
    root = tree.getroot()
    data = [
        # [instructionID, operation, adress] 
    ]

    for instruction in root:
        data.append([int(instruction[0].text), instruction[1].text, int(instruction[2].text)])
    return data
