#!/usr/bin/env python3"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = (AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    '''
    sets up handling for incoming clients.
    :return: 
    '''
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." %client_address)
        client.send(bytes("Greetings from the cave!"+"Now type your name and press enter!","utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):#Takes client socket as argument
    '''
    Handlers a single client connection
    :param client: 
    :return: 
    '''
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'welcome %s! If you ever want to quit, type{quit} to exit.'%name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!"%name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name)


