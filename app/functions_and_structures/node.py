from app.functions_and_structures.position import Position


class Node:
    """
    A class representing a node for A* algorithm\n
    `position` - cartesian representation of node's position (type: `Position`)
    """

    def __init__(self, position: Position = None):
        self._position = position

        self.g = 0
        self.h = 0
        self.f = 0

        self.traversable = True
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
