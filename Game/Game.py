from collections import Counter


class Game:
    def __init__(self):
        self.board = {7: ' ', 8: ' ', 9: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      1: ' ', 2: ' ', 3: ' '}
        self.finished = False
        self.player_one = None
        self.player_two = None
        self.player_one_character = "X"
        self.player_two_character = "O"

    def announce_game_start(self):
        self.player_one.sendall(f"The game has begun!MESSAGEEND".encode())
        self.player_one.sendall(f"Your character is {self.player_one_character}MESSAGEEND".encode())
        self.player_two.sendall(f"The game has begun!MESSAGEEND".encode())
        self.player_two.sendall(f"Your character is {self.player_two_character}MESSAGEEND".encode())

    def print_board(self):
        board = self.board[7] + '|' + self.board[8] + '|' + self.board[9] + \
                "\n-+-+-\n" + \
                self.board[4] + '|' + self.board[5] + '|' + self.board[6] + \
                "\n-+-+-\n" + \
                self.board[1] + '|' + self.board[2] + '|' + self.board[3]
        self.player_one.sendall(f"{board}MESSAGEEND".encode())
        self.player_two.sendall(f"{board}MESSAGEEND".encode())

    def get_occurrences(self):
        x_occurrences = Counter(self.board.values())["X"]
        o_occurrences = Counter(self.board.values())["O"]
        return x_occurrences, o_occurrences

    def find_turn(self, x_occurrences, o_occurrences):
        if x_occurrences <= o_occurrences:
            player = self.player_one
            character = self.player_one_character
            self.player_one.sendall(f"It's your turnMESSAGEEND".encode())
            self.player_two.sendall(f"Player one's turnMESSAGEEND".encode())
        else:
            player = self.player_two
            character = self.player_two_character
            self.player_one.sendall(f"Player two's turnMESSAGEEND".encode())
            self.player_two.sendall(f"It's your turnMESSAGEEND".encode())
        return player, character

    def validate_position(self, position):
        if (position > 0) and (position < 10):
            current_value = self.board.get(position)
            if (current_value == " ") or (current_value is None):
                return True, None
            else:
                return False, "Entered position is already filled!"
        else:
            return False, "Not a valid input!"

    def update_board(self, position, character):
        self.board[position] = character

    def take_turn(self, player, character):
        valid_position = False
        while not valid_position:
            player.sendall(f"INPUTMESSAGEEND".encode())
            player.sendall(f"Enter grid position:MESSAGEEND".encode())
            position = player.recv(1024)
            position = int.from_bytes(position, "big")
            valid_position, message = self.validate_position(position)
            if not valid_position:
                player.sendall((message + "MESSAGEEND").encode())
        self.update_board(position, character)

    def check_victory(self):
        victory = False
        victor = None
        loser = None
        starting_points_groups = [[7, 8, 9], [7, 4, 1], [7], [9]]
        increments = [-3, 1, -2, -4]
        for starting_points in starting_points_groups:
            increment = increments[starting_points_groups.index(starting_points)]
            for starting_point in starting_points:
                values = []
                for _ in range(3):
                    value = self.board.get(starting_point)
                    values.append(value)
                    starting_point += increment
                if len(set(values)) == 1:
                    if values[0] == "X":
                        victor = self.player_one
                        loser = self.player_two
                        victory = True
                    elif values[0] == "O":
                        victor = self.player_two
                        loser = self.player_one
                        victory = True
        return victory, victor, loser

    def check_tie(self):
        if " " in self.board.values():
            return False
        else:
            return True

    def announce_victory(self, victor, loser):
        victor.sendall(f"The game is over!\nYou have won the game!MESSAGEEND".encode())
        loser.sendall(f"The game is over!\nBetter luck next timeMESSAGEEND".encode())

    def announce_tie(self):
        self.player_one.sendall(f"The game is over!\nIt's a tie!MESSAGEEND".encode())
        self.player_two.sendall(f"The game is over!\nIt's a tie!MESSAGEEND".encode())

    def end_game(self):
        self.player_one.sendall(f"ENDMESSAGEEND".encode())
        self.player_two.sendall(f"ENDMESSAGEEND".encode())

    def play_game(self):
        game_end = False
        self.announce_game_start()
        self.print_board()
        while not game_end:
            x_occurrences, o_occurrences = self.get_occurrences()
            player, character = self.find_turn(x_occurrences, o_occurrences)
            self.take_turn(player, character)
            self.print_board()
            game_end, victor, loser = self.check_victory()
            if game_end:
                self.announce_victory(victor, loser)
            else:
                game_end = self.check_tie()
                if game_end:
                    self.announce_tie()
        self.end_game()
