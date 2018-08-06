def parse(file):
    return [[int(w) for w in line.split(',')]
            for line in open(file).read().splitlines()]


# Dijkstra's algorithm specialised to the case of a grid with adjacent nodes
# connected. Since we have weighted nodes rather than weighted edges, treat the
# weight of an edge from A to B as the weight of B.
def dijkstra(matrix, initial, target):
    unvisited = {(x, y)
                 for y in range(len(matrix)) for x in range(len(matrix[y]))}
    distances = {initial: matrix[initial[1]][initial[0]]}

    while target in unvisited:
        (x, y) = min(
            (node for node in unvisited if node in distances),
            key=lambda node: distances[node])

        unvisited_neighbors = ((xp, yp) for (xp, yp) in
                               ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                               if (xp, yp) in unvisited)

        for (xp, yp) in unvisited_neighbors:
            if (xp, yp) not in distances or distances[(
                    x, y)] + matrix[yp][xp] < distances[(xp, yp)]:
                distances[(xp, yp)] = distances[(x, y)] + matrix[yp][xp]

        unvisited.remove((x, y))

    return distances[target]


print(dijkstra(parse('data/083'), (0, 0), (79, 79)))
