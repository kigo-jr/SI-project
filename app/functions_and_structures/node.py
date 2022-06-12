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
        self.__traversable = not barrier
        self.__open = not barrier
        self.__closed = not barrier
        self.__start = not barrier
        self.__end = not barrier
        self.__path = not barrier

    @property
    def closed(self) -> bool:
        return self.__closed

    @closed.setter
    def closed(self, closed: bool) -> None:
        self.__closed = closed
        self.__traversable = not closed
        self.__open = not closed
        self.__barrier = not closed
        self.__start = not closed
        self.__end = not closed
        self.__path = not closed

    @property
    def open(self) -> bool:
        return self.__open

    @open.setter
    def open(self, open: bool) -> None:
        self.__open = open
        self.__traversable = not open
        self.__closed = not open
        self.__barrier = not open
        self.__start = not open
        self.__end = not open
        self.__path = not open

    @property
    def path(self) -> bool:
        return self.__path

    @path.setter
    def path(self, path: bool) -> None:
        self.__path = path
        self.__traversable = not path
        self.__closed = not path
        self.__barrier = not path
        self.__start = not path
        self.__end = not path
        self.__open = not path

    @property
    def start(self) -> bool:
        return self.__start

    @start.setter
    def start(self, start: bool) -> None:
        self.__start = start
        self.__traversable = not start
        self.__closed = not start
        self.__barrier = not start
        self.__path = not start
        self.__end = not start
        self.__open = not start

    @property
    def end(self) -> bool:
        return self.__end

    @end.setter
    def end(self, end: bool) -> None:
        self.__end = end
        self.__traversable = not end
        self.__closed = not end
        self.__barrier = not end
        self.__path = not end
        self.__start = not end
        self.__open = not end

    @property
    def traversable(self) -> bool:
        return self.__traversable or self.end or self.start

    @traversable.setter
    def traversable(self, traversable: bool) -> None:
        self.__traversable = traversable
        self.__end = not traversable
        self.__closed = not traversable
        self.__barrier = not traversable
        self.__path = not traversable
        self.__start = not traversable
        self.__open = not traversable

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

    @property
    def symbol(self) -> str:
        if self.start:
            return "S"
        if self.end:
            return "E"
        if self.path:
            return "*"
        if self.closed:
            return "^"
        if self.open:
            return "%"
        if self.barrier:
            return "@"
        if self.traversable:
            return " "

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
        self.traversable = True
