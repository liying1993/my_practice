import socket
from threading import Thread
from queue import Queue

def recv_data(con):
    try:
        data = con.recv(1024)
        if len(data)>0:
            print("get it")
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
            connection, client_address = sock.accept()
            p = Thread(target=recv_data, args=(connection,))
            p.start()
    except Exception as e:
        print(e)
    finally:
        sock.close()

if __name__ == '__main__':
    my_sock()

