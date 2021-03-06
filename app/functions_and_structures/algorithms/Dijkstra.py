from queue import PriorityQueue
from app.functions_and_structures.grid import *
import pygame


def search(window, grid):
    window.draw()
    start = grid.start
    end = grid.end
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = {start}
    came_from = {}

    f_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score[start] = 0

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        node = open_set.get()[2]
        open_set_hash.remove(node)
        if node == end:
            reconstruct_path(came_from, end, window, start, end)
            return True

        for neighbour in grid.get_possible_moves(node):
            temp_score = f_score[node] + neighbour.cost
            if temp_score < f_score[neighbour]:
                came_from[neighbour] = node
                f_score[neighbour] = temp_score
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    if neighbour != start and neighbour != end:
                        neighbour.open = True

            window.draw()

        if node != start and node != end:
            node.closed = True
