#!/usr/bin/python3
import abc
import pygame


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

    @abc.abstractmethod
    def __enter__(self):
        raise NotImplementedError("Renderer is an abstract class")

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError("Renderer is an abstract class")


class PyGameRenderer(Renderer):
    """PyGame based rendering"""
    def __init__(self, _grid):
        super().__init__(_grid)

    def render(self):
        pass

    def __enter__(self):
        pygame.init()
        screen = pygame.display.set_mode((468, 60))
        pygame.display.set_caption('Monkey Fever')
        pygame.mouse.set_visible(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    grid = Grid(100, 100)
    p1 = Path(grid, Pos(5, 10), Pos(24, 18))

    with PyGameRenderer(grid) as renderer:
        renderer.render()