import curses
from traffic import Renderer

__author__ = 'danielb'


class CursesRenderer(Renderer):
    """Curses based rendering"""
    def __init__(self, _grid):
        super().__init__(_grid)

    def __enter__(self):
        self._scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self._scr.keypad(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        curses.nocbreak()
        curses.echo()
        self._scr.keypad(0)
        curses.endwin()

    def line(self, path):
        s = path.start
        e = path.end
        if (e.y-s.y) < (e.x-s.x):
            d = (e.y-s.y)/(e.x-s.x)
            for x in range(s.x, e.x):
                y = s.y+(d*(x-s.x))
                self._scr.addch(int(y), int(x), '¤')
        else:
            for y in range(s.y, e.y):
                d = (e.x-s.x)/(e.y-s.y)
                x = s.x+(d*(y-s.y))
                self._scr.addch(int(y), int(x), '¤')

    def render(self):
        self._scr.addstr(str(self._grid))
        for p in self._grid.paths:
            self.line(p)
        self._scr.getch()