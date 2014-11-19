#!/usr/bin/python3
import abc
import curses


class Grid:
    """The main area"""
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return "[{},{}]".format(self._width, self._height)


class Pos:
    """A position in the grid"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "({}, {})".format(self._x, self._y)


class Path:
    """A path in the grid"""
    def __init__(self, _grid, start, end):
        self._grid = _grid
        self._start = start
        self._end = end

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

    def render(self):
        self._scr.addstr(str(self._grid))
        self._scr.getch()


if __name__ == '__main__':
    grid = Grid(100, 100)
    p1 = Path(grid, Pos(10, 10), Pos(10, 20))
    print(p1)

    with CursesRenderer(grid) as renderer:
        renderer.render()