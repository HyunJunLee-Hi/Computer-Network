#이현준
#2016025887

import socket

host1 = '127.0.0.1'
port1 = 4000
buf = 1024
address1 = (host1, port1)
#IPv4 / TCP
client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect(address1)
#send a message to server
client_socket1.sendall('client1 message'.encode())
#message from server
message = client_socket1.recv(buf)
print(message.decode())

client_socket1.close()

