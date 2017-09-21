import socket
from threading import Thread
from queue import Queue

def recv_data(con):
    try:
        data = con.recv(1024)
        print("=================")
        print(data)
        filename = data.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n'%(len(outputdata))
        con.send(header.encode())
        for i in range(0, len(outputdata)):
            con.send(outputdata[i].encode())
        con.close()
        # if len(data)>0:
        #     print("get it")
    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        con.send(header.encode())
    except Exception as e:
        print(e)
    finally:
        con.close()

def my_sock():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 8899)
    sock.bind(server_address)

    sock.listen(8)
    try:
        while 1:
            print('Ready to serve......')
            connection, client_address = sock.accept()
            p = Thread(target=recv_data, args=(connection,))
            p.start()
    except Exception as e:
        print(e)
    finally:
        sock.close()

if __name__ == '__main__':
    my_sock()





# from socket import *
# serverSocket = socket(AF_INET, SOCK_STREAM)
# address = ('', 6789)
# serverSocket.bind(address)
# serverSocket.listen(1)
#
# while 1:
#     print('Ready to serve......')
#     connectionSocket, addr = serverSocket.accept()
#     try:
#         message = connectionSocket.recv(1024)
#         print(message)
#         filename = message.split()[1]
#         f = open(filename[1:])
#         outputdata = f.read()
#         header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n'%(len(outputdata))
#         connectionSocket.send(header.encode())
#
#         for i in range(0, len(outputdata)):
#             connectionSocket.send(outputdata[i].encode())
#         connectionSocket.close()
#     except IOError:
#         header = 'HTTP/1.1 404 Not Found'
#         connectionSocket.send(header.encode())
#
#
# serverSocket.close()
