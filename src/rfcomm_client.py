import bluetooth as bt

bd_addr = "01:23:45:67:89:AB"

port = 1

sock = bt.BluetoothSocket(bt.RFCOMM)
sock.connect((bd_addr, port))

sock.send("Hello from a Bluetooth connection :) !")

sock.close()
