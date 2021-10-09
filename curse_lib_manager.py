from curses import wrapper
from krestiki0 import GameController


def main(stdscr):

    # def clear_screen(self):
    #     self.screen.clear()
    #
    # def add_to_screen(self, string_to_add):
    #     self.screen.addstr(0, 0, string_to_add)
    #     self.screen.refresh()
    #
    # def get_input_1(self):
    #     return self.X

    game_ = GameController(screen=stdscr)
    game_.start_game()


wrapper(main)
