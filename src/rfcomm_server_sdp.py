import bluetooth as bt

server_socket = bt.BluetoothSocket(bt.RFCOMM)
server_socket.bind(("", bt.PORT_ANY))
server_socket.listen(1)

port = server_socket.getsockname()[1]

print("listening on port %d" % port)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
bt.advertise_service(server_socket, "FooBar", service_id=uuid,
                     service_classes=[uuid, bt.SERIAL_PORT_CLASS],
                     profiles=[bt.SERIAL_PORT_PROFILE])

print("listening on port %d" % port)

client_socket, address = server_socket.accept()
print("Accepted connection from", address)

data = client_socket.recv(1024)
print("reveived [%s]" % data)

client_socket.close()
server_socket.close()
