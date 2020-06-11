import bluetooth as bt

server_socket = bt.BluetoothSocket(bt.RFCOMM)

port = bt.get_available_port(bt.RFCOMM)
server_socket.bind(("", port))
server_socket.listen(1)

print("listening on port %d" % port)

uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
bt.advertise_service(server_socket, "FooBar service", uuid)

client_socket, address = server_socket.accept()
print("Accepted connection from", address)

data = client_socket.recv(1024)
print("reveived [%s]" % data)

client_socket.close()
server_socket.close()
