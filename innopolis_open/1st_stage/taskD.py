def floyd_warshall(n, graph):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

n = int(input().strip())
graph = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    graph.append(row)

result = floyd_warshall(n, graph)

for row in result:
    print(' '.join(map(str, row)))
