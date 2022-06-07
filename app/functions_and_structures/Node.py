from app.functions_and_structures.Position import Position


class Node:
    """
    A class representing a node for A* algorithm\n
    `position` - cartesian representation of node's position (type: `Position`)
    """

    def __init__(self, position: Position = None):
        self._position = position

        self._g = 0
        self._h = 0
        self._f = 0

        self._traversable = True
        self._neighbours = []

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.position == __o.position
        return False

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, g):
        self._g = g

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, f):
        self._f = f

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def traversable(self):
        return self._traversable

    @traversable.setter
    def traversable(self, traversable: bool = True):
        self._traversable = traversable

    @property
    def neighbours(self):
        return self._neighbours

    @neighbours.setter
    def neighbours(self, neighbours):
        self._neighbours = neighbours

    def init_neighbours(self, grid):
        self.neigbours = []
        height = len(grid)
        width = 0
        if height != 0:
            width = len(grid[0])

        if not (height != 0 and width != 0): return

        if self.y < height - 1 and grid[self.position.y + 1][self.position.x].traversable:
            self.neighbours.append(grid[self.position.y + 1][self.position.x])
