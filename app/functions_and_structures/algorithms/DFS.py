from app.functions_and_structures.grid import *


def search(start, end):
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
                child.visited = True
                q.append(child)
                # TODO
                if child == end:
                    return path_from(node)
