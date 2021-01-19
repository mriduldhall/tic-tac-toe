from Game.Client import Client


class CLI:
    def __init__(self):
        pass

    def initiate(self):
        exit_initiated = False
        client = Client()
        while True:
            message = (client.socket.recv(1024)).decode()
            if message == "END":
                break
            else:
                print(message)
        client.socket.close()
