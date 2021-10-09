# -*- coding: utf-8 -*-

import os
import time
from random import randint
from curses import wrapper
from screen import Screen


os.environ['TERM'] = 'xterm'


# UZD 1 pabaigti zaidima krestiki ir noliky:):
# 1.1 priskirti gieztai X ir O zaidejams ~ Done su skintamaisiais
# 1.1 sukurti priesininko ejimo algoritma ~ Done randominis (Challenge sukurti geresni)
# 1.2 sukurti zaidimo laimejimo algoritma  ~ Done
# 1.3 Neleisti zaidejui pildyti uzpildytu celiu
# 1.4 Tikrinti userio ivedamus simbolius, apriboti galimybe ivedimui (leisti tik 1-9)
# 1.5 Padaryti, kad butu galima pasirinkti pradzioje, kas eis pirmas
# 1.6 Padaryti kad du automatai galetu zaisti pries save, ir kad butu galima tureti Ai zaidejus, kurie eina pagal
# skirtingus algoritmus.
class Cell:
    def __init__(self, nr_):
        self.nr = nr_ + 1
        self.content = '-'

    def __repr__(self):
        return f"Celė {self.nr}:  {self.content}"


class Board:
    def __init__(self, screen=None):
        self.cells = [Cell(e) for e in range(9)]
        self.screen = screen

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

    def display_board(self, message1=None, message2=None):
        self.screen.draw(self.format_template(message1=message1, message2=message2))


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
    def __init__(self, screen=None):
        self.board = Board(screen)
        self.game_symbols = ['X', 'O']
        self.screen = Screen('curse')
        self.player_symbol = screen and screen.getkey() or input("Choose your play symbol (X/O): ")
        self.ai_symbol = list(self.game_symbols)
        self.ai_symbol.remove(self.player_symbol)
        self.ai_symbol = self.ai_symbol[0]
        self.oponent_ai = OpponentAi(self.ai_symbol)
        self.state = ''
        self.current_player = 'user'

    def reset_board(self):
        self.board = Board()

    def check_if_won(self):
        winner = ''
        win = False
        check_map = [
            (1, 2, 3),  # pirma horizontali eilute is virsaus
            (4, 5, 6),  # pirma horizontali eilute is virsaus
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7)
        ]
        game_cells = self.board.cells
        for check_tuple in check_map:
            cells_to_check = [c_ for c_ in game_cells if c_.nr in check_tuple]
            # print(cells_to_check)
            unique_content = set()
            for i in cells_to_check:
                unique_content.add(i.content)
            # print(unique_content)
            if len(unique_content) == 1:
                uni_con = list(unique_content)[0]
                if uni_con == '-':
                    pass
                else:  # vieta, kur pazymi, kad laimejo
                    win = True
                    if uni_con == self.ai_symbol:
                        winner = self.oponent_ai.name
                    else:
                        winner = 'player'
        return win, winner

    def get_user_input(self):
        if self.screen:
            return self.screen.getkey()
        else:
            return input("Target a cell (1-9): ")

    def propagate_game(self):
        user_input = self.get_user_input()
        # Userio inputo patikros funcija galetu buti cia kvieciama (1.3, 1.4)
        selected_cell = int(user_input)
        cell_obj = self.board.cells[selected_cell -1]
        cell_obj.content = self.player_symbol
        # CHECK IF GAME NOT WON (If yes change GameController state)
        # Patikrinti ar zaidimas nelaimetas, o jei taip pakeisti Game Controlelio steita i done
        win, winner = self.check_if_won()
        if win:
            self.state = 'done'
            self.board.display_board(
                message1=f"Game over!",
                message2=f'{winner} won !!!'
            )
            return
        # display board, kas laimejo.
        # daryti return
        #######################
        self.board.display_board(
            message1=f"Game ON!",
            message2=f'{ self.oponent_ai.name.upper() } TURN !!!'
        )
        time.sleep(3)
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
        win, winner = self.check_if_won()
        if win:
            self.state = 'done'
            self.board.display_board(
                message1=f"Game over!",
                message2=f'{winner} won !!!'
            )
            return
        # display board, kas laimejo.
        # daryti return
        #######################

    def start_game(self):
        cc = CurseController()
        with cc as controller:
            controller.addstr()
            print('uuu')
        # self.board.display_board(
        #     message1=f"Hello, you will playing against {self.oponent_ai.name}",
        #     message2='YOUR TURN !!!'
        # )
        # while self.state != 'done':
        #     self.propagate_game()

        # Ideti user inputa, kuris paklausia ar po laimejimo nori dar zaisti
        # jei nori, tada paleisti ta pacia funcija is naujo, nutrynus lenta
        # user_input = input("Want to try again? (Y/N): ")
        # if str(user_input).strip() == 'Y':
        #     self.start_game()


if __name__ == "__main__":
    game_ = GameController()
    game_.start_game()
