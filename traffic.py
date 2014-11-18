import abc


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

    def render(self):
        pass


if __name__ == '__main__':
    grid = Grid(100, 100)
    p1 = Path(grid, Pos(10, 10), Pos(10, 20))
    print(p1)

    renderer = CursesRenderer(grid)
    renderer.render()