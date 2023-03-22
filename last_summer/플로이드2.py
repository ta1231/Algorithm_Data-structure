INF = 1e9
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    if graph[a][b] > cost:
        graph[a][b] = cost

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=' ')
    print()
