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


def test(draw, grid):
    draw()
    start = grid.start
    end = grid.end
    start_node = start
    q = [start_node]
    start_node.visited = True
    while len(q) > 0:
        node = q.pop(0)
        # TODO get possible moves function in grid
        children = Grid.get_possible_moves(node)
        for child in children:
            if not child.visited:
                child.parent = node
                child.visited = True  # Might be wrong
                q.append(child)
                if child == end:
                    return path_from(node)
        draw()
    return None
