import socket


class Client:
    def __init__(self):
        self.socket = self.create_socket()
        # self.name = self.get_details()

    @staticmethod
    def create_socket():
        HOST = '127.0.0.1'
        PORT = 65432
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        return client_socket

    def get_details(self):
        name = input("Enter your name:")
        self.socket.sendall(name.encode())
        return name
