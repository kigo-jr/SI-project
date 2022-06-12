from operator import le
from typing import List
from app.functions_and_structures import Position
from app.functions_and_structures import Node


class Grid:
    """
    Class representing the grid on which maze can be constructed.

    """

    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width = width
        self.height = height
        self.grid = [[Node(Position(i, j)) for i in range(width)] for j in range(height)]
        for i in range(self.height):
            self.grid[i][0].barrier = True
            self.grid[i][self.width - 1].barrier = True
        for i in range(self.width):
            self.grid[0][i].barrier = True
            self.grid[self.height - 1][i].barrier = True

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

    @property
    def has_start(self) -> bool:
        for row in self.grid:
            for node in row:
                if node.start:
                    return True
        return False

    @property
    def has_end(self) -> bool:
        for row in self.grid:
            for node in row:
                if node.end:
                    return True
        return False

    # TODO find neighbours who are not visited (node state)
    def get_possible_moves(self, node: Node) -> List[Node]:

        pass
        # code from lab1 SI same as update_neighbours in main2.py
        # possible_movements = []
        # if node.y - 1 >= 0 and self.maze[node.y - 1][node.x].type != '#':  # north
        #     possible_movements.append(self.maze[node.y - 1][node.x])
        # if node.x + 1 < len(self.maze[node.y]) and self.maze[node.y][node.x + 1].type != '#':  # east
        #     possible_movements.append(self.maze[node.y][node.x + 1])
        # if node.y + 1 < len(self.maze) and self.maze[node.y + 1][node.x].type != '#':  # south
        #     possible_movements.append(self.maze[node.y + 1][node.x])
        # if node.x - 1 >= 0 and self.maze[node.y][node.x - 1].type != '#':  # west
        #     possible_movements.append(self.maze[node.y][node.x - 1])
        #
        # return possible_movements


def path_from(self, node):
    path = [node]
    while node.parent is not None:
        node = node.parent
        path.append(node)
    return path


def make_grid(width=10, height=10):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(Node(Position(j, i)))
