from enum import Enum
from typing import Tuple
from app.functions_and_structures import Position


class Node_Types(Enum):
    pass


class Node:
    """
    A class representing a node for A* algorithm\n
    `position` - cartesian representation of node's position (type: `Position`)
    """

    colours = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "orange": (255, 168, 0),
        "gray": (128, 128, 128),
        "turquoise": (64, 224, 208)
    }

    def __init__(self, position: Position = None):
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

        self.traversable = True  # FIXME don't know if it is the same as visited
        self.barrier = False
        self.open = False
        self.closed = False
        self.path = False
        self.start = False
        self.end = False
        self.parent = None
        self.neighbours = []

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.position == __o.position
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, g):
        self.__g = g

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, f):
        self.__f = f

    @property
    def position(self) -> Position:
        return self.__position

    @position.setter
    def position(self, position) -> None:
        self.__position = position

    @property
    def barrier(self) -> bool:
        return self.__barrier

    @barrier.setter
    def barrier(self, barrier: bool) -> None:
        self.__barrier = barrier
        self.traversable = not barrier

    @property
    def closed(self) -> bool:
        return self.__closed

    @closed.setter
    def closed(self, closed: bool) -> None:
        self.__closed = closed
        if closed:
            self.open = False

    @property
    def open(self) -> bool:
        return self.__open

    @open.setter
    def open(self, open: bool) -> None:
        self.__open = open
        if open:
            self.closed = False

    @property
    def path(self) -> bool:
        return self.__path

    @path.setter
    def path(self, path: bool) -> None:
        self.__path = path

    @property
    def start(self) -> bool:
        return self.__start

    @start.setter
    def start(self, start: bool) -> None:
        if self.barrier:
            return
        self.__start = start

    @property
    def end(self) -> bool:
        return self.__end

    @end.setter
    def end(self, end: bool) -> None:
        if self.barrier:
            return
        self.__end = end

    @property
    def traversable(self) -> bool:
        return self.__traversable

    @traversable.setter
    def traversable(self, traversable: bool) -> None:
        self.__traversable = traversable

    @property
    def neighbours(self):
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, neighbours) -> None:
        self.__neighbours = neighbours

    @property
    def x(self) -> int:
        return self.position.x

    @property
    def y(self) -> int:
        return self.position.y

    @property
    def colour(self) -> Tuple[int, int, int]:
        if self.start:
            return Node.colours["orange"]
        if self.end:
            return Node.colours["turquoise"]
        if self.path:
            return Node.colours["purple"]
        if self.closed:
            return Node.colours["red"]
        if self.open:
            return Node.colours["green"]
        if self.barrier:
            return Node.colours["black"]
        if self.traversable:
            return Node.colours["white"]

    def __str__(self) -> str:
        return f"Node({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Node(Position({self.x}, {self.y}))"

    def init_neighbours(self, grid) -> None:
        self.neighbours = []
        height = len(grid)
        width = 0
        if height != 0:
            width = len(grid[0])

        if not (height != 0 and width != 0): return

        if self.y < height - 1 and grid[self.y + 1][self.x].traversable:
            self.neighbours.append(grid[self.y + 1][self.x])
        if self.y > 0 and grid[self.y - 1][self.x].traversable:
            self.neighbours.append(grid[self.y - 1][self.x])
        if self.x < width - 1 and grid[self.y][self.x + 1].traversable:
            self.neighbours.append(grid[self.y][self.x + 1])
        if self.x > 0 and grid[self.y][self.x - 1].traversable:
            self.neighbours.append(grid[self.y][self.x - 1])

    def reset(self) -> None:
        self.barrier = False
        self.closed = False
        self.open = False
        self.start = False
        self.end = False
        self.traversable = True
