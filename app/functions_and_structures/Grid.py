from app.functions_and_structures.Position import *
from app.functions_and_structures.Node import *


def make_grid(width=10, height=10):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(Node(Position(j, i)))



