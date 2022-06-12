from app.functions_and_structures.grid import *


def search(window, grid):
    window.draw()
    start = grid.start
    end = grid.start
    start_node = start
    q = [start_node]
    start_node.visited = True
    while len(q) > 0:
        node = q.pop(-1)
        node.visited = True

        if node == end:
            return path_from(node)

        # TODO get possible moves function in grid
        children = Grid.get_possible_moves(node)
        for child in children:
            if not child.visited:
                child.parent = node
                child.visited = True  # Might be wrong
                q.append(child)
        window.draw()
    return None
