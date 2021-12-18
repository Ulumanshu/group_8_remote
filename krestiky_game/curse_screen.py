import curses


class CurseScreenContext:

    def __init__(self):
        self.screen = None
        self.colors = {
            'white': curses.COLOR_WHITE,
            'red': curses.COLOR_RED,
            'green': curses.COLOR_GREEN,
            'yellow': curses.COLOR_YELLOW,
            'blue': curses.COLOR_BLUE,
            'magenta': curses.COLOR_MAGENTA,
            'cyan': curses.COLOR_CYAN,
            'black': curses.COLOR_BLACK
        }

    def __enter__(self):
        # opening and sharing of resources
        curses.wrapper(self.init_screen)
        return self

    def __exit__(self, type, value, traceback):
        # cleaning, release of resources
        print("END OF CURSE SCREEN!!!")

    def init_screen(self, stdscr):
        self.screen = stdscr
        self.set_pairs()

    def get_color(self, color_index):
        return curses.color_pair(color_index)

    def set_pairs(self):
        curses.init_pair(1, self.colors['white'], self.colors['black'])
        curses.init_pair(2, self.colors['red'], self.colors['black'])
        curses.init_pair(3, self.colors['yellow'], self.colors['black'])
        curses.init_pair(4, self.colors['blue'], self.colors['black'])
