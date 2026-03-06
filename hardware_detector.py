import wmi

# Function to detect GPU information

def detect_gpus():
    c = wmi.WMI()
    gpus = []
    for gpu in c.Win32_VideoController():
        gpus.append(gpu.Name)
    return gpus

# Function to detect motherboard information

def detect_motherboard():
    c = wmi.WMI()
    for board in c.Win32_BaseBoard():
        return board.Product

# Function to detect BIOS version

def detect_bios():
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        return bios.SMBIOSBIOSVersion

# Function to detect chipset information (this may vary depending on the system)

def detect_chipset():
    c = wmi.WMI()
    for chipset in c.Win32_Chipset():
        return chipset.Name

# Main function to gather all information

def main():
    gpus = detect_gpus()
    motherboard = detect_motherboard()
    bios = detect_bios()
    chipset = detect_chipset()
    
    print("Detected GPUs:", gpus)
    print("Motherboard:", motherboard)
    print("BIOS Version:", bios)
    print("Chipset:", chipset)

if __name__ == '__main__':
    main()