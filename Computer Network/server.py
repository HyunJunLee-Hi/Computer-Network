#이현준
#2016025887

import socket

host = ''
port = 4000
buf = 1024
address = (host, port)
#IPv4 / TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind(Every address/port 4000)
server_socket.bind(address)
#listen
server_socket.listen()
#client connect
client_socket, addr = server_socket.accept()


while 1:

    #message from client
    message = client_socket.recv(buf)
    if not message:
        break
    print(addr,'/' , message.decode())
    message = 'server message'
    #send a message to client
    client_socket.sendall(message.encode())


client_socket.close()
server_socket.close()
