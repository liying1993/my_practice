from socket import *
from threading import Thread
import os
import re
def get_request_name_from_http(http):
    r = re.search(r"GET /(.+?) ", http)
    fileName = ""
    if r != None:
        fileName = r.group(1)
    return fileName
def writeHtml(client, fileName):
    rspHead = None
    rspBody = None
    if not os.path.exists(fileName):
        rspHead = "HTTP/1.1 404 error\r\nServer: foreverServer\r\n\r\n"
        rspBody = "file not found"
    else:
        rspHead = "HTTP/1.1 200 OK\r\nServer: foreverServer\r\n\r\n"
        html = open(fileName, 'r', encoding='UTF-8')
        rspBody = html.read()
    client.send((rspHead + rspBody).encode("utf-8"))
def deal_socket(client):
    print("-------开启新的线程----------")
    try:
        data = client.recv(1024)
        if len(data) > 0:
            fileName = get_request_name_from_http(data.decode("utf-8"))
            writeHtml(client, fileName)
    finally:
        client.close()
        print("-------关闭新的线程----------")
def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    address = ('', 9876)
    server.bind(address)
    server.listen(10)
    try:
        while True:
            print("-------等待接受服务----------")
            client, client_address = server.accept()
            print("-------接受服务成功----------")
            # 就这里和多线程不同，并且千万不能把client关掉
            p = Thread(target=deal_socket, args=(client,))
            p.start()
    except Exception as e:
        print(e)
    finally:
        server.close()
        print("-------服务结束----------")
if __name__ == "__main__":
    main()