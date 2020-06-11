from bluetooth import *

rpi_addr = "B8:27:EB:B0:CD:7A"

port = 1

s = BluetoothSocket(RFCOMM)
s.connect((rpi_addr, port))
s.send("Hola madre sos fea... ugh I mean bonita :)")
s.close()
