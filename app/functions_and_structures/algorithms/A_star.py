from queue import PriorityQueue
from time import sleep
from app.functions_and_structures.node import *
import pygame


def a_star(window, grid):
    start = grid.start
    end = grid.end
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score = {spot: float("inf") for row in grid.grid for spot in row}

    g_score[start] = 0
    f_score[start] = h(start, end)

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]  # get usuwa i zwraca krotkę ()
        open_set_hash.remove(current)  #
        if current == end:
            reconstruct_path(came_from, end, window, start, end)
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.position, end.position)
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    if neighbour != start and neighbour != end:
                        neighbour.open = True
            window.draw()

        if current != start and current != end:
            current.closed = True


def h(start: Node = None, end: Node = None) -> int:
    if start and end:
        return abs(start.x - end.x) + abs(start.y + end.y)
    return None


def g(start: Node = None, end: Node = None):
    pass


def reconstruct_path(came_from, current, window, start, end):
    while current in came_from:
        current = came_from[current]
        if current != start and current != end:
            current.path = True
        window.draw()
