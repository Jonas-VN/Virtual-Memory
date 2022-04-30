from functions import parse_data

FYSIEKE_ADRESRUIMTE = 48 * pow(2, 10) # 48 KB
VIRTUELE_ADRESRUIMTE = pow(2, 16) # 64 KB
GROOTTE_FRAME = pow(2, 12) # 4 KB

AANTAL_FRAMES_FYSIEK = FYSIEKE_ADRESRUIMTE // GROOTTE_FRAME
AANTAL_FRAMES_VIRTUEEL = VIRTUELE_ADRESRUIMTE // GROOTTE_FRAME


def een_instructie_uitvoeren(instructie):
    if instructie[1] == "Read":
        pass
    elif instructie[1] == "Write":
        pass
    elif instructie[1] == "Start":
        pass
    elif instructie[1] == "Terminate":
        pass


data = parse_data("Instructions_20000_4.xml")
for instructie in data:
    een_instructie_uitvoeren(instructie)
