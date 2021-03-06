from app.functions_and_structures.grid import *
import pygame


def search(window, grid):
    window.draw()
    start = grid.start
    end = grid.end
    q = [start]
    came_from = {}

    while len(q) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        node = q.pop(0)
        if node == end:
            reconstruct_path(came_from, end, window, start, end)
            return True

        for neighbour in grid.get_possible_moves(node):
            came_from[neighbour] = node
            if neighbour not in q:
                q.append(neighbour)
                if neighbour != start and neighbour != end:
                    neighbour.open = True

            window.draw()

        if node != start and node != end:
            node.closed = True
