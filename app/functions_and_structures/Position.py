class Position:
    """A class, representing a point in cartesian plane,
       used in nodes of graph."""

    def __init__(self, x=None, y=None):
        self._x = x
        self._y = y

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.x == __o.x and self.y == __o.y
        return False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
