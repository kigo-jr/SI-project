from app.functions_and_structures.grid import *


def search(start, end):
    start_node = start
    q = [start_node]
    start_node.visited = True
    while len(q) > 0:
        node = q.pop(0)
        node.visited = True

        if node == end:
            return path_from(node)

        children = Grid.get_possible_moves(node)
        for child in children:
            if not child.visited:
                cost = (len(path_from(child))-1)
                if child.parent == None:
                    child.f = cost
                    child.parent = node
                    child.visited = True  # Might be wrong
                    q.append(child)
                elif cost < child.f:
                    child.f = cost
                    child.parent = node

        q.sort(key=lambda x: x.cost)

    return None