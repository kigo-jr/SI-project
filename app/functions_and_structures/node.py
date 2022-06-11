from typing import Tuple
from app.functions_and_structures import Position


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
        self._position = position

        self.g = 0
        self.h = 0
        self.f = 0

        self.traversable = True  # FIXME don't know if it is the same as visited
        self.is_barrier = False
        self.visited = False
        self.parent = None
        self.neighbours = []

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.position == __o.position
        return False

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
        return self._f

    @f.setter
    def f(self, f):
        self.__f = f

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def traversable(self):
        return self.__traversable

    @traversable.setter
    def traversable(self, traversable: bool = True):
        self.__traversable = traversable

    @property
    def neighbours(self):
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, neighbours):
        self.__neighbours = neighbours

    @property
    def x(self) -> int:
        return self.position.x

    @property
    def y(self) -> int:
        return self.position.y

    @property
    def colour(self) -> Tuple[int, int, int]:
        if self.is_barrier:
            return Node.colours["black"]
        if self.visited:
            return Node.colours["red"]
        if self.traversable:
            return Node.colours["white"]

    def __str__(self) -> str:
        return f"Node({self.position.x}, {self.position.y})"

    def __repr__(self) -> str:
        return f"Node(Position({self.position.x}, {self.position.y}))"

    def init_neighbours(self, grid):
        self.neigbours = []
        height = len(grid)
        width = 0
        if height != 0:
            width = len(grid[0])

        if not (height != 0 and width != 0): return

        if self.y < height - 1 and grid[self.position.y + 1][self.position.x].traversable:
            self.neighbours.append(grid[self.position.y + 1][self.position.x])
