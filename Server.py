#!/usr/bin/env python3

import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.bind((HOST, PORT))
        socket.listen()
        connection, address = socket.accept()
        with connection:
            print("Connected by", address)
            connection.sendall(b"Table goes here")
