from queue import PriorityQueue
from app.functions_and_structures.Position import *
from app.functions_and_structures.Node import *


def make_grid(width=10, height=10):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(Node(Position(j, i)))


def a_star(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    f_score = {spot: float("inf") for row in grid for spot in row}

    g_score[start] = 0
    f_score[start] = h(start, end)

    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2] #  get usuwa i zwraca krotkę ()
        open_set_hash.remove(current) #  
        if current == end:
            pass

        for neighbour in current.neighbours:
            pass
        pass

def h(start: Node=None, end: Node=None) -> int:
    if start and end:
        return abs(start.position.x - end.position.x) + abs(start.position.y + end.position.y)
    return None

def g(start: Node=None, end: Node=None):
    pass