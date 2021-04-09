#이현준
#2016025887

import socket

host2 = '127.0.0.1'
port2 = 4000
buf = 1024
address2 = (host2, port2)
#IPv4 / TCP
client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket2.connect(address2)
#send a message to server
client_socket2.sendall('client2 message'.encode())
#message from server
message = client_socket2.recv(buf)
print(message.decode())

client_socket2.close()
