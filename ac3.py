from hall import *


def AC3(arcs: list[tuple[Hall, Hall]]) -> bool:
    queue = [i for i in arcs]

    while (len(queue)):
        h1, h2 = queue.pop()
        if (revise(h1, h2)):

            # If there is no remaining domain value for h1
            if len(h1.domain) == False:
                return False

            # Find all neighbors of h1
            h1Neighbors = []
            for arc in arcs:
                if (arc[0].hallName == h1.hallName and arc[1].hallName != h2.hallName):
                    h1Neighbors.append(arc[1])

            # Iterate through all neighbors of h1
            for neighbor in h1Neighbors:
                queue.append((neighbor, h1))

    return True


def revise(h1: Hall, h2: Hall) -> bool:
    revised = False

    for d1 in h1.domain:
        if (len(h2.domain) == 1 and h2.domain[0] == d1):
            h1.domain.remove(d1)
            revised = True

    return revised
