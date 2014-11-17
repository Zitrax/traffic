# A grid representing the area
# A Traveller ? representing entities travelling through the grid


class Grid(object):
    """The main area"""
    def __init__(self, width, height):
        self._width = width
        self._height = height


class Pos(object):
    """A position in the grid"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "({}, {})".format(self._x, self._y)


class Path(object):
    """A path in the grid"""
    def __init__(self, _grid, start, end):
        self._grid = _grid
        self._start = start
        self._end = end

    def __str__(self):
        return "[{} -> {}]".format(self._start, self._end)


if __name__ == '__main__':
    grid = Grid(100, 100)
    p1 = Path(grid, Pos(10, 10), Pos(10, 20))
    print(p1)