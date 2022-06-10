class Position:
    """A class, representing a point in cartesian plane,
       used in nodes of graph."""

    def __init__(self, x: int=None, y: int=None):
        if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
            self.x = x
            self.y = y

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.x == __o.x and self.y == __o.y
        else:
            raise Exception(f"Comparing objects of incompatibile types: {type(self)} and {type(__o)}")

    @property
    def x(self) -> int:
        return self.x

    @x.getter
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x) -> None:
        if isinstance(x, int) and x >= 0:
            self.__x = x
        else:
            raise Exception(f"X axis position must be non-negative integer value!\nProvided value: {x}")

    @property
    def y(self) -> int:
        return self.y

    @y.getter
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y) -> None:
        if isinstance(y, int) and y >= 0:
            self.__y = y
        else:
            raise Exception(f"Y axis position must be a non-negative integer value!\nProvided value: {y}")
