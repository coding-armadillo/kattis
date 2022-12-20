from itertools import combinations

while True:
    n = int(input())
    if n == -1:
        break
    graph = {}
    for i in range(n):
        graph[str(i)] = [str(v) for v, e in zip(range(n), input().split()) if e == "1"]

    # listing the weak vertices ordered from least to greatest
    # I guess it means vertex number, not the weakness
    # keys = sorted(graph, key=lambda x: len(graph[x]), reverse=True)

    keys = graph.keys()

    result = []

    for key in keys:

        has_triangle = False
        for a, b in combinations(graph[key], 2):
            if a in graph[b] and b in graph[a]:
                has_triangle = True
                break

        if not has_triangle:
            result.append(key)

    print(" ".join(result))
