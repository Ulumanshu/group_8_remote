# -*- coding: utf-8 -*-

import time
from random import randint
from screen import Screen


class Cell:
    def __init__(self, nr_):
        self.nr = nr_ + 1
        self.content = '-'

    def __repr__(self):
        return f"Celė {self.nr}:  {self.content}"


class Board:

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

    def __init__(self, screen=None):
        self.cells = [Cell(e) for e in range(9)]
        self.screen = screen

    def format_template(self, message1=None, message2=None):
        rendered_template = f"""
~ KRESTIKY Y NOLIKY X/O !o()~/!!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{ message1 or ''}
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
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
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

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
        # mid_cel = [cell_ for cell_ in cells if cell_.nr == 5][0]
        # Controll own win
        for check_tuple in Board.check_map:
            cells_to_check = [c_ for c_ in cells if c_.nr in check_tuple]
            free_cells = [_c_ for _c_ in cells_to_check if _c_.content == '-']
            own_cells = [_c_ for _c_ in cells_to_check if _c_.content == self.ai_symbol]
            if len(free_cells) == 1 and len(own_cells) == 2:
                free_cells[0].content = self.ai_symbol
                return
        # Controll oponent win
        for check_tuple in Board.check_map:
            cells_to_check = [c_ for c_ in cells if c_.nr in check_tuple]
            free_cells = [_c_ for _c_ in cells_to_check if _c_.content == '-']
            oponent_cells = [_c_ for _c_ in cells_to_check if _c_.content not in ['-', self.ai_symbol]]
            if len(free_cells) == 1 and len(oponent_cells) == 2:
                free_cells[0].content = self.ai_symbol
                return

        # if mid_cel.content == '-':
        #     mid_cel = [cell_ for cell_ in valid_cells if cell_.nr == 5][0]
        #     mid_cel.content = self.ai_symbol

        else:
            # Randomly choose most free path
            potential_paths = []
            for check_tuple in Board.check_map:
                cells_to_check = [c_ for c_ in cells if c_.nr in check_tuple]
                potential_cells = [_c_ for _c_ in cells_to_check if _c_.content in ['-', self.ai_symbol]]
                if len(potential_cells) == 3:
                    potential_paths.append(check_tuple)

            rand_range = len(potential_paths)
            if rand_range > 0:
                chosen_path = potential_paths[randint(0, rand_range - 1)]
                cells_to_check = [c_ for c_ in cells if c_.nr in chosen_path]
                free_cells = [_c_ for _c_ in cells_to_check if _c_.content == '-']
                rand_range_ = len(free_cells)
                if rand_range_ > 0:
                    chosen_cell = valid_cells[randint(0, rand_range_ - 1)]
                    chosen_cell.content = self.ai_symbol
                    return

            #Randomly choose anything
            rand_range = len(valid_cells)
            if rand_range > 0:
                chosen_cell = valid_cells[randint(0, rand_range - 1)]
                chosen_cell.content = self.ai_symbol


class GameController:
    def __init__(self):
        self.screen = Screen('curse').screen
        self.get_color = self.screen.get_color
        self.board = Board(self.screen)
        self.game_symbols = ['X', 'O']
        self.player_symbol = 'X' #  self.screen.user_input("Choose your play symbol (X/O): ")
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
        game_cells = self.board.cells
        for check_tuple in Board.check_map:
            cells_to_check = [c_ for c_ in game_cells if c_.nr in check_tuple]
            unique_content = set()
            for i in cells_to_check:
                unique_content.add(i.content)
            if len(unique_content) == 1:
                uni_con = list(unique_content)[0]
                if uni_con == '-':
                    pass
                else:
                    win = True
                    if uni_con == self.ai_symbol:
                        winner = self.oponent_ai.name
                    else:
                        winner = 'Player 1'

        return win, winner

    def check_if_draw(self):
        res = False
        free_cells = [_c_.nr for _c_ in self.board.cells if _c_.content == '-']
        if len(free_cells) == 0:
            res = True

        return res

    def get_user_input(self, input_string):
        return self.screen.user_input(draw_string=input_string, x=10, y=25, color=self.get_color(2))

    def reselect(self):
        free_cells = [_c_.nr for _c_ in self.board.cells if _c_.content == '-']
        user_input = self.get_user_input(f"Target a free cell from ({', '.join(map(str, free_cells))}): ")
        try:
            selected_cell = int(user_input.strip())
            if selected_cell not in free_cells:
                selected_cell = self.reselect()
        except:
            selected_cell = self.reselect()

        return selected_cell

    def player_turn(self):
        self.screen.clear_screen()
        self.board.display_board(
            message1=f"Game ON!",
            message2=f'YOUR TURN !!!'
        )
        user_input = self.get_user_input("Target a cell (1-9): ")
        free_cells = [_c_.nr for _c_ in self.board.cells if _c_.content == '-']
        try:
            selected_cell = int(user_input.strip())
            if selected_cell not in free_cells:
                selected_cell = self.reselect()
        except:
            selected_cell = self.reselect()

        cell_obj = self.board.cells[selected_cell - 1]
        cell_obj.content = self.player_symbol

        win, winner = self.check_if_won()
        if win:
            self.display_win(winner)
        elif self.check_if_draw():
            self.display_draw()
        else:
            self.board.display_board(
                message1=f"RIP IT:)",
                message2=f'{self.oponent_ai.name.upper()} TURN !!!',
            )

        return win

    def ai_turn(self):
        self.oponent_ai.make_a_move(self.board.cells)
        self.board.display_board(
            message1=f"Game ON!",
            message2=f'{self.oponent_ai.name.upper()} TURN !!!',
        )
        win, winner = self.check_if_won()
        if win:
            self.display_win(winner)
        elif self.check_if_draw():
            self.display_draw()
        else:
            self.board.display_board(
                message1=f"RIP IT:)",
                message2='YOUR TURN !!!',
            )

        return win

    def display_win(self, winner):
        self.board.display_board(
            message1=f"Game over!",
            message2=f'{winner} won !!!',
        )
        self.state = 'done'
        self.screen.user_input('THE END', x=10, y=25, color=self.get_color(3))

    def display_draw(self):
        self.board.display_board(
            message1=f"Game Over!",
            message2='DRAW !!!',
        )
        self.state = 'done'
        self.screen.user_input('THE END', x=10, y=25, color=self.get_color(3))

    def propagate_game(self):
        win = self.player_turn()
        time.sleep(2)
        if not win:
            self.ai_turn()
        self.screen.user_input(x=0, y=25)
        time.sleep(1)

    def start_game(self):
        while self.state != 'done':
            self.propagate_game()


if __name__ == "__main__":
    game_ = GameController()
    game_.start_game()
