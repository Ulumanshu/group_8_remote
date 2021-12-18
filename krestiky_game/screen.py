import os
from curse_screen import CurseScreenContext


class Screen:
    def __init__(self, type=None):
        valid_types = {
            'curse': self.init_curse_screen,
            "terminal": self.init_terminal_screen,
        }
        self.type = type in valid_types and type or 'terminal'
        self.screen = valid_types.get(self.type)()

    def init_curse_screen(self):
        return CurseScreen()

    def init_terminal_screen(self):
        return TerminalScreen()


class CurseScreen:

    def __init__(self):
        with CurseScreenContext() as screen_obj:
            self.screen = screen_obj.screen
            self.colors = screen_obj.colors
            self.get_color = screen_obj.get_color

    def clear_screen(self):
        self.screen.clear()

    def draw(self, draw_string=None, x=0, y=0):
        self.clear_screen()
        self.screen.addstr(y, x, draw_string or '')
        self.screen.refresh()

    def user_input(self, draw_string=None, x=0, y=0, color=None):
        color = color or self.get_color(1)
        if draw_string:
            self.screen.addstr(y, x, draw_string or '', color)
            self.screen.refresh()
        return self.screen.getkey(y, x + (draw_string and len(draw_string) or 0))


class TerminalScreen:

    def __init__(self):
        os.environ['TERM'] = 'xterm'

    def clear_screen(self):
        os.system('clear')

    def draw(self, draw_string=None, x=0, y=0):
        print("I ASM USED")
        print(draw_string)

    def user_input(self, draw_string=None, x=0, y=0):
        return input(draw_string or '')
