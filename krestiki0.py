# -*- coding: utf-8 -*-

import os
import time
from random import randint

os.environ['TERM'] = 'xterm'


# UZD 1 pabaigti zaidima krestiki ir noliky:):
# 1.1 priskirti gieztai X ir O zaidejams
# 1.1 sukurti priesininko ejimo algoritma
# 1.2 sukurti zaidimo laimejimo algoritma
class Cell:
    def __init__(self, nr_):
        self.nr = nr_ + 1
        self.content = '-'


class Board:
    def __init__(self):
        self.cells = [Cell(e) for e in range(9)]

    def format_template(self, message1=None, message2=None):
        rendered_template = f"""
~ KRESTIKY Y NOLIKY X/O !o()~/!!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{ message1 or ''}
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
|----1----|----2----|----3----|
|         |         |         |
|    { self.cells[0].content }    |    { self.cells[1].content }    |    { self.cells[2].content }    |
|         |         |         |
|----4----|----5----|----6----|
|         |         |         |
|    { self.cells[3].content }    |    { self.cells[4].content }    |    { self.cells[5].content }    |
|         |         |         |
|----7----|----8----|----9----|
|         |         |         |
|    { self.cells[6].content }    |    { self.cells[7].content }    |    { self.cells[8].content }    |
|         |         |         |
|---------|---------|---------|
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

{ message2 or ''}
"""

        return rendered_template

    @staticmethod
    def clear_console():
        os.system('clear')

    def display_board(self, message1=None, message2=None):
        self.clear_console()
        print(self.format_template(message1=message1, message2=message2))


class OpponentAi:
    def __init__(self, game_symbol):
        self.name = 'Petras I'
        self.ai_symbol = game_symbol

    def make_a_move(self, cells):
        valid_cells = [cell for cell in cells if cell.content == '-']
        rand_range = len(valid_cells)
        if rand_range > 0:
            chosen_cell = valid_cells[randint(0, rand_range - 1)]
            chosen_cell.content = self.ai_symbol


class GameController:
    def __init__(self):
        self.board = Board()
        self.game_symbols = ['X', 'O']
        self.player_symbol = input("Choose your play symbol (X/O): ")
        self.ai_symbol = list(self.game_symbols)
        self.ai_symbol.remove(self.player_symbol)
        self.ai_symbol = self.ai_symbol[0]
        self.oponent_ai = OpponentAi(self.ai_symbol)
        self.state = ''

    def reset_board(self):
        self.board = Board()

    def get_user_input(self):
        user_input = input("Target a cell (1-9): ")
        selected_cell = int(user_input)
        cell_obj = self.board.cells[selected_cell -1]
        cell_obj.content = self.player_symbol
        # CHECK IF GAME NOT WON (If yes change GameController state)
        # Patikrinti ar zaidimas nelaimetas, o jei taip pakeisti Game Controlelio steita i done
        # display board, kas laimejo.
        # daryti return
        #######################
        self.board.display_board(
            message1=f"Game ON!",
            message2=f'{ self.oponent_ai.name.upper() } TURN !!!'
        )
        time.sleep(1)
        # NOW LET AI PLACE ITS X OR Y
        # Padaryti ejima su AI
        self.oponent_ai.make_a_move(self.board.cells)
        #############################
        self.board.display_board(
            message1=f"RIP IT:)",
            message2='YOUR TURN !!!'
        )
        # CHECK IF GAME NOT WON (If yes change GameController state)
        # Patikrinti ar zaidimas nelaimetas, o jei taip pakeisti Game Controlerio steita i done
        # display board, kas laimejo.
        # daryti return
        #######################

    def start_game(self):
        self.board.display_board(
            message1=f"Hello, you will playing against {self.oponent_ai.name}",
            message2='YOUR TURN !!!'
        )
        while self.state != 'done':
            self.get_user_input()


if __name__ == "__main__":
    game_ = GameController()
    game_.start_game()

# check_map = [
#     (1, 2, 3),  # pirma horizontali eilute is virsaus
#     (4, 5, 6),  # pirma horizontali eilute is virsaus
# ]