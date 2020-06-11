import sys
import bluetooth as bt

uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
service_matches = bt.find_services(uuid)

if (len(service_matches)) == 0:
    print("couldn't find the FooBar service")
    sys.exit(1)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to '%s' on '%s'" % (name, host))

socket = bt.BluetoothSocket(bt.RFCOMM)
socket.connect((host, port))
socket.send("Hello world!")
socket.close()
