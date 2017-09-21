import socket
import sys
"""
socket作为服务器
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 8888)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            print('receive {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
