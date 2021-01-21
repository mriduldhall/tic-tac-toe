class Game:
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}
        self.finished = False
        self.player_one = None
        self.player_two = None
        self.player_one_character = "X"
        self.player_two_character = "O"

    def announce_game_start(self):
        self.player_one.sendall("The game has begun!".encode())
        self.player_one.sendall(f"\nYour character is {self.player_one_character}".encode())
        self.player_two.sendall("The game has begun!".encode())
        self.player_two.sendall(f"\nYour character is {self.player_two_character}".encode())

    def print_board(self):
        board = self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'] + \
                "\n-+-+-\n" + \
                self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'] + \
                "\n-+-+-\n" + \
                self.board['1'] + '|' + self.board['2'] + '|' + self.board['3']
        self.player_one.sendall(f"{board}".encode())
        self.player_two.sendall(f"{board}".encode())

    def end_game(self):
        self.player_one.sendall("END".encode())
        self.player_two.sendall("END".encode())

    def play_game(self):
        game_end = False
        self.announce_game_start()
        self.print_board()
        self.end_game()
        while not game_end:
            pass
