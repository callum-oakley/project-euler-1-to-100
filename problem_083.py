# Dijkstra's algorithm specialised to the case of a grid with adjacent nodes
# connected. Since we have weighted nodes rather than weighted edges, treat the
# weight of an edge from A to B as the weight of B.
def dijkstra(n, weight, neighbors, target):
    unvisited = {(x, y) for y in range(n) for x in range(n)}
    distances = {(0, 0): weight((0, 0))}

    def d(v):
        return distances[v]

    while target in unvisited:
        current = min((v for v in unvisited if v in distances), key=d)

        for v in (v for v in neighbors(current) if v in unvisited):
            if v not in distances or d(current) + weight(v) < d(v):
                distances[v] = d(current) + weight(v)

        unvisited.remove(current)

    return d(target)


def neighbors(v):
    x, y = v
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def main():
    matrix = [
        [int(w) for w in line.split(",")]
        for line in open("data/083").readlines()
    ]

    def weight(v):
        x, y = v
        return matrix[y][x]

    return dijkstra(
        len(matrix), weight, neighbors, (len(matrix) - 1, len(matrix) - 1)
    )
    # 425185
