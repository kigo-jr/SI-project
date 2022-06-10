from typing import List
from app.functions_and_structures.position import Position
from app.functions_and_structures.node import Node

class Grid:

    """
    Class representing the grid on which maze can be constructed.

    """

    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width = width
        self.height = height
        self.grid = [[Node(Position(i, j)) for i in range(width)] for j in range(height)]

    @property
    def grid(self) -> List[List[Node]]:
        return self.__grid

    @grid.setter
    def grid(self, grid: List[List[Node]]) -> None:
        self.__grid = grid

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        if isinstance(width, int) and width > 0:
            self.__width = width
        else:
            raise Exception(f"Width must be non-negative integer value!\nProvided value {width}")

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        if isinstance(height, int) and height > 0:
            self.__height = height
        else:
            raise Exception(f"Height must be non-negative integer value!\nProvided value {height}")



def make_grid(width=10, height=10):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(Node(Position(j, i)))



