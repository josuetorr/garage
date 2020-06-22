import sys
import bluetooth as bt

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
name = "FooBar"
service_matches = bt.find_service(name, uuid)

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
