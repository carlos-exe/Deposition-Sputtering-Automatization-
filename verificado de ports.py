from serial.tools import list_ports

ports = list_ports.comports()
for port in ports:
    print(f"Puerto encontrado: {port.device}, {port.description}")