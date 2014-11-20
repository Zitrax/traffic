#!/usr/bin/python3
import abc
import curses


class Grid:
    """The main area"""
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._paths = []

    def add_path(self, path):
        self._paths.append(path)

    @property
    def paths(self):
        return self._paths

    def __str__(self):
        return "[{},{}]".format(self._width, self._height)


class Pos:
    """A position in the grid"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return "({}, {})".format(self._x, self._y)


class Path:
    """A path in the grid"""
    def __init__(self, _grid, start, end):
        self._start = start
        self._end = end
        grid.add_path(self)

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __str__(self):
        return "[{} -> {}]".format(self._start, self._end)


class Renderer(metaclass=abc.ABCMeta):
    """Interface for rendering the grid"""
    def __init__(self, _grid):
        self._grid = _grid

    @abc.abstractmethod
    def render(self):
        """Render the grid to screen"""
        raise NotImplementedError("Renderer is an abstract class")


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


if __name__ == '__main__':
    grid = Grid(100, 100)
    p1 = Path(grid, Pos(5, 10), Pos(24, 18))

    with CursesRenderer(grid) as renderer:
        renderer.render()