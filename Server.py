#!/usr/bin/env python3

import socket
import threading
from Game.Game import Game


def launch_game(game):
    game.play_game()


def get_players(socket):
    socket.listen()
    player_one, player_one_address = socket.accept()
    player_one.sendall("Welcome player one\nWaiting for player two...MESSAGEEND".encode())
    socket.listen()
    player_two, player_two_address = socket.accept()
    player_two.sendall("Welcome player twoMESSAGEEND".encode())
    return player_one, player_one_address, player_two, player_two_address


def create_game(player_one, player_two):
    game = Game()
    game.player_one = player_one
    game.player_two = player_two
    return game


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.bind((HOST, PORT))
        while True:
            player_one, player_one_address, player_two, player_two_address = get_players(socket)
            game = create_game(player_one, player_two)
            game_thread = threading.Thread(target=launch_game, args=[game])
            game_thread.start()
