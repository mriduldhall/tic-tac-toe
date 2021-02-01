from Game.Client import Client


class Exit:
    def __init__(self):
        self.is_exit_initiated = False

    def execute(self):
        print("Exiting...")
        self.is_exit_initiated = True

    def exit_initiated(self):
        return self.is_exit_initiated


class Help:
    def __init__(self):
        pass

    def execute(self):
        print("Help(WIP)")

    @staticmethod
    def exit_initiated():
        return False


class StartGame:
    def __init__(self):
        pass

    def execute(self):
        Client().initiate()

    @staticmethod
    def exit_initiated():
        return False


class CLI:
    def __init__(self):
        self.menu_dict = {
            "s": StartGame(),
            "h": Help(),
            "e": Exit(),
        }

    def initiate(self):
        print("Welcome to Tic Tac Toe")
        exit_initiated = False
        while not exit_initiated:
            choice = input("Enter s to start a game, h for help and e to exit:")
            menu_item = self.menu_dict.get(choice)
            if menu_item is None:
                print("Please enter a valid choice")
                continue
            menu_item.execute()
            exit_initiated = menu_item.exit_initiated()
