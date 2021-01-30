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

    def end(self):
        print("Game is over!")
        # message = (self.socket.recv(1024)).decode()
        # print(message)
        self.socket.close()
        return True

    def input(self, message=None):
        print("In Input")
        if not message:
            message = (self.socket.recv(1024)).decode()
        else:
            message = (message.split("MESSAGEEND"))[0]
        position = int(input(message))
        self.socket.sendall(bytes([position]))
        return False

    def index_in_list(self, list, index):
        return index < len(list)

    def initiate(self):
        flags = {
            "END": self.end,
            "INPUT": self.input,
        }
        exit_initiated = False
        while not exit_initiated:
            message = (self.socket.recv(1024)).decode()
            messages = message.split("MESSAGEEND")
            del messages[len(messages)-1]
            message_position = 0
            for message in messages:
                flag = flags.get(message)
                if flag is not None:
                    if (flag == self.input) and self.index_in_list(messages, message_position+1):
                        exit_initiated = flag(messages[message_position+1])
                        del messages[message_position+1]
                    else:
                        exit_initiated = flag()
                else:
                    print(message)
                message_position += 1
