from hashlib import new
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

        for row in self.grid:
            for node in row:
                node.init_neighbours(self.grid)

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

    @property
    def start(self) -> Node:
        for row in self.grid:
            for node in row:
                if node.start:
                    return node
        return None

    @property
    def end(self) -> Node:
        for row in self.grid:
            for node in row:
                if node.end:
                    return node
        return None

    def reset(self) -> None:
        for row in self.grid:
            for node in row:
                node.reset()

    def update_neighbours(self) -> None:
        for row in self.grid:
            for node in row:
                node.init_neighbours(self.grid)

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            for row in self.grid:
                line = ""
                for node in row:
                    line += node.symbol
                line += "\n"
                f.write(line)

    def load(self, path: str) -> None:
        with open(path, "r") as f:
            new_grid = []
            for y_index, line in enumerate(f.readlines()):
                new_row = []
                for x_index, char in enumerate(line):
                    new_row.append(Node(Position(x_index, y_index)))
                    if char == "@":
                        new_row[x_index].barrier = True
                    elif char == "S":
                        new_row[x_index].start = True
                    elif char == "E":
                        new_row[x_index].end = True
                new_grid.append(new_row)
        self.grid = new_grid




    # TODO find neighbours who are not visited (node state)
    def get_possible_moves(self, node: Node) -> List[Node]:
        possible_moves = []
        for neighbour in node.neighbours:
            if neighbour.open or neighbour.traversable:
                possible_moves.append(neighbour)
        return possible_moves

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

def reconstruct_path(came_from, current, window, start, end):
    while current in came_from  and current != start:
        current = came_from[current]
        if current != start and current != end:
            current.path = True
        window.draw()


def make_grid(width=10, height=10):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(Node(Position(j, i)))
