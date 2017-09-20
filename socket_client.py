import socket
import sys

'''
socket 作为客户端
'''
#创建一个TCP/IP 连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接某个端口的socket，并且正准备接受数据
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b"This is the message, It will be repeated."
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()
