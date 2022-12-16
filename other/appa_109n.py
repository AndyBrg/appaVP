
def rotorcode(x):
    return {      
    b"\x00": "OFF",
    b"\x01": "V",
    b"\x02": "mV",
    b"\x03": "Ohm",
    b"\x04": "Diode",
    b"\x05": "mA",
    b"\x06": "A",
    b"\x07": "Cap.",
    b"\x08": "Hz",
    b"\x09": "Temp."
}[x]


def bluecode(x):
    return {    
    b"\x01\x00": "AC",
    b"\x01\x01": "DC",
    b"\x01\x02": "AC+DC",
    b"\x02\x00": "AC",
    b"\x02\x01": "DC",
    b"\x02\x02": "AC+DC",
    b"\x03\x00": "Ohm",
    b"\x03\x01": "Low Ohm",
    b"\x03\x02": "-------",
    b"\x04\x00": "Diode",
    b"\x04\x01": "Beeper",
    b"\x04\x02": "-------",    
    b"\x05\x00": "AC",
    b"\x05\x01": "DC",
    b"\x05\x02": "AC+DC",   
    b"\x06\x00": "AC",
    b"\x06\x01": "DC",
    b"\x06\x02": "AC+DC",  
    b"\x07\x00": "Cap",
    b"\x07\x01": "-------",
    b"\x07\x02": "-------",   
    b"\x08\x00": "Hz",
    b"\x08\x01": "Duty Factor",
    b"\x08\x02": "-------", 
    b"\x09\x00": "deg.C",   
    b"\x09\x01": "deg.F",
    b"\x09\x02": "-------"
}[x]

def rangecode(x):
    return {
    b"\x01\x00\x00": "2V",      # AC V        Auto
    b"\x01\x00\x01": "20V",     # AC V        Auto
    b"\x01\x00\x02": "200V",    # AC V        Auto
    b"\x01\x00\x03": "1000V",   # AC V        Auto
    b"\x01\x01\x00": "2V",      # DC V        Auto
    b"\x01\x01\x01": "20V",     # DC V        Auto
    b"\x01\x01\x02": "200V",    # DC V        Auto
    b"\x01\x01\x03": "1000V",   # DC V        Auto
    b"\x01\x02\x00": "2V",      # (AC+DC) V   Auto
    b"\x01\x02\x01": "20V",     # (AC+DC) V   Auto
    b"\x01\x02\x02": "200V",    # (AC+DC) V   Auto
    b"\x01\x02\x03": "1000V",   # (AC+DC) V   Auto
    b"\x02\x00\x00": "20m",     # AC mV       Auto
    b"\x02\x00\x01": "200mV",   # AC mV       Auto
    b"\x02\x01\x00": "20mV",    # DC mV       Auto
    b"\x02\x01\x01": "200mV",   # DC mV       Auto
    b"\x02\x02\x00": "20mV",    # (AC+DC) mV  Auto
    b"\x02\x02\x01": "200mV",   # (AC+DC) mV  Auto
    b"\x01\x00\x80": "2V",      # AC V        Manual
    b"\x01\x00\x81": "20V",     # AC V        Manual
    b"\x01\x00\x82": "200V",    # AC V        Manual
    b"\x01\x00\x83": "1000V",   # AC V        Manual
    b"\x01\x01\x80": "2V",      # DC V        Manual
    b"\x01\x01\x81": "20V",     # DC V        Manual
    b"\x01\x01\x82": "200V",    # DC V        Manual
    b"\x01\x01\x83": "1000V",   # DC V        Manual
    b"\x01\x02\x80": "2V",      # (AC+DC) V   Manual
    b"\x01\x02\x81": "20V",     # (AC+DC) V   Manual
    b"\x01\x02\x82": "200V",    # (AC+DC) V   Manual
    b"\x01\x02\x83": "1000V",   # (AC+DC) V   Manual
    b"\x02\x00\x80": "20m",     # AC mV       Manual
    b"\x02\x00\x81": "200mV",   # AC mV       Manual
    b"\x02\x01\x80": "20mV",    # DC mV       Manual
    b"\x02\x01\x81": "200mV",   # DC mV       Manual
    b"\x02\x02\x80": "20mV",    # (AC+DC) mV  Manual
    b"\x02\x02\x81": "200mV",   # (AC+DC) mV  Manual    
    b"\x05\x00\x00": "2V",      # AC mA       Auto
    b"\x05\x00\x01": "20V",     # AC mA       Auto
    b"\x05\x01\x00": "2V",      # DC mA       Auto
    b"\x05\x01\x01": "20V",     # DC mA       Auto
    b"\x05\x02\x00": "2V",      # (AC+DC) mA  Auto
    b"\x05\x02\x01": "20V",     # (AC+DC) mA  Auto  
    b"\x05\x00\x80": "2V",      # AC mA       Manual
    b"\x05\x00\x81": "20V",     # AC mA       Manual
    b"\x05\x01\x80": "2V",      # DC mA       Manual
    b"\x05\x01\x81": "20V",     # DC mA       Manual
    b"\x05\x02\x80": "2V",      # (AC+DC) mA  Manual
    b"\x05\x02\x81": "20V",     # (AC+DC) mA  Manual  
    b"\x03\x00\x00": "200Ohm",  # Ohm         Auto
    b"\x03\x00\x01": "2kOhm",   # Ohm         Auto
    b"\x03\x00\x02": "20kOhm",  # Ohm         Auto
    b"\x03\x00\x03": "200kOhm", # Ohm         Auto
    b"\x03\x00\x04": "2MOhm",   # Ohm         Auto
    b"\x03\x00\x05": "20MOhm",  # Ohm         Auto
    b"\x03\x01\x00": "2kOhm",   # Low Ohm     Auto
    b"\x03\x01\x01": "20kOhm",  # Low Ohm     Auto
    b"\x03\x01\x02": "200kOhm", # Low Ohm     Auto
    b"\x03\x01\x03": "2MOhm",   # Low Ohm     Auto
    b"\x03\x01\x04": "20MOhm",  # Low Ohm     Auto
    b"\x07\x00\x00": "4nF",     # Cap         Auto
    b"\x07\x00\x01": "40nF",    # Cap         Auto
    b"\x07\x00\x02": "400nF",   # Cap         Auto
    b"\x07\x00\x03": "4uF",     # Cap         Auto
    b"\x07\x00\x04": "40uF",    # Cap         Auto
    b"\x07\x00\x05": "400uF",   # Cap         Auto
    b"\x07\x00\x06": "4mF",     # Cap         Auto
    b"\x07\x00\x07": "40mF",    # Cap         Auto    
    b"\x08\x00\x00": "20Hz",    # Hz          Auto
    b"\x08\x00\x01": "200Hz",   # Hz          Auto
    b"\x08\x00\x02": "2kHz",    # Hz          Auto
    b"\x08\x00\x03": "20kHz",   # Hz          Auto
    b"\x08\x00\x04": "200kHz",  # Hz          Auto
    b"\x08\x00\x05": "1MHz",    # Hz          Auto    
    b"\x09\x00\x00": "400",     # deg.C       Auto
    b"\x09\x00\x01": "1200",    # deg.C       Auto
    b"\x09\x01\x00": "400",     # deg.F       Auto
    b"\x09\x01\x01": "2192",    # deg.F       Auto
    b"\x03\x00\x80": "200Ohm",  # Ohm         Manual
    b"\x03\x00\x81": "2kOhm",   # Ohm         Manual
    b"\x03\x00\x82": "20kOhm",  # Ohm         Manual
    b"\x03\x00\x83": "200kOhm", # Ohm         Manual
    b"\x03\x00\x84": "2MOhm",   # Ohm         Manual
    b"\x03\x00\x85": "20MOhm",  # Ohm         Manual
    b"\x03\x01\x80": "2kOhm",   # Low Ohm     Manual
    b"\x03\x01\x81": "20kOhm",  # Low Ohm     Manual
    b"\x03\x01\x82": "200kOhm", # Low Ohm     Manual
    b"\x03\x01\x83": "2MOhm",   # Low Ohm     Manual
    b"\x03\x01\x84": "20MOhm",  # Low Ohm     Manual
    b"\x07\x00\x80": "4nF",     # Cap         Manual
    b"\x07\x00\x81": "40nF",    # Cap         Manual
    b"\x07\x00\x82": "400nF",   # Cap         Manual
    b"\x07\x00\x83": "4uF",     # Cap         Manual
    b"\x07\x00\x84": "40uF",    # Cap         Manual
    b"\x07\x00\x85": "400uF",   # Cap         Manual
    b"\x07\x00\x86": "4mF",     # Cap         Manual
    b"\x07\x00\x87": "40mF",    # Cap         Manual    
    b"\x08\x00\x80": "20Hz",    # Hz          Manual
    b"\x08\x00\x81": "200Hz",   # Hz          Manual
    b"\x08\x00\x82": "2kHz",    # Hz          Manual
    b"\x08\x00\x83": "20kHz",   # Hz          Manual
    b"\x08\x00\x84": "200kHz",  # Hz          Manual
    b"\x08\x00\x85": "1MHz",    # Hz          Manual    
    b"\x09\x00\x80": "400",     # deg.C       Manual
    b"\x09\x00\x81": "1200",    # deg.C       Manual
    b"\x09\x01\x80": "400",     # deg.F       Manual
    b"\x09\x01\x81": "2192"     # deg.F       Manual
}.get(x, "None")


def pointcode(x):
    return {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4
}[x]


def unitcode(x):
    return {    
    "00000": "None",
    "00001": "V",
    "00010": "mV",
    "00011": "A",
    "00100": "mA",
    "00101": "dB",
    "00110": "dBm",
    "00111": "nF",
    "01000": "uF",
    "01001": "mF",
    "01010": "\u03A9",
    "01011": "K\u03A9",
    "01100": "M\u03A9",
    "01101": "G\u03A9",
    "01110": "%",
    "01111": "Hz",
    "10000": "KHz",
    "10001": "MHz",
    "10010": "\u00B0С",
    "10011": "\u00B0F",
    "10100": "s",
    "10101": "ms",
    "10110": "ns",
    "10111": "V",
    "11000": "mV",
    "11001": "A",
    "11010": "mA",
    "11011": "\u03A9",
    "11100": "K\u03A9",
    "11101": "M\u03A9"
}[x]



def functiontable(x):
    return {        
    b"\x00": "None",
    b"\x01": "Input Reading",
    b"\x02": "Freq",
    b"\x03": "Period",
    b"\x04": "Duty Factor",
    b"\x08": "Stamp (Store, Recall,Login,Logout)",
    b"\x09": "Store",
    b"\x0A": "Recall",
    b"\x0C": "Auto Hold",
    b"\x0D": "Max",
    b"\x0E": "Min",
    b"\x10": "Peak Hold Max",
    b"\x11": "Peak Hold Min",
    b"\x17": "\u0394",
    b"\x19": "Ref",
    b"\x1A": "dBm",
    b"\x1B": "dB",
    b"\x25": "Avg",
    b"\x26": "ProbE",
    b"\x27": "Er",
    b"\x28": "FUSE",
    b"\x29": "PAUS",
    b"\x2A": "Logout Max data",
    b"\x2B": "Logout Min data",
    b"\x2C": "Logout Max Turning Point",
    b"\x2D": "Logout Min Turning Point",
    b"\x2E": "Logout data",
    b"\x2F": "Period Time",
    b"\x30": "FULL",
    b"\x31": "EPEr",
    b"\x32": "EEPROM",
    b"\x33": "Login Stamp"
}[x]

