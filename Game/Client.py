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
        try:
            client_socket.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Something went wrong!")
            return None
        return client_socket

    def get_details(self):
        name = input("Enter your name:")
        self.socket.sendall(name.encode())
        return name

    def end(self):
        self.socket.close()
        return True

    def input(self, message=None):
        if not message:
            message = (self.socket.recv(1024)).decode()
            message = (message.split("MESSAGEEND"))[0]
        valid_input = False
        while not valid_input:
            try:
                position = int(input(message))
                self.socket.sendall(bytes([position]))
            except ValueError:
                print("Invalid input!")
            else:
                valid_input = True
        return False

    @staticmethod
    def index_in_list(list, index):
        return index < len(list)

    def initiate(self):
        if not self.socket:
            return
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
