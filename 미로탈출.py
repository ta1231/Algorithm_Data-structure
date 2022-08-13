n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(start_x, start_y):
    q = [(start_x, start_y)]
    while q:
        nx, ny = q.pop()
        for i in range(4):
            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m:
                if graph[nx + dx[i]][ny + dy[i]] == 1:
                    graph[nx + dx[i]][ny + dy[i]] = graph[nx][ny] + 1
                    q.append((nx + dx[i], ny + dy[i]))


dfs(0, 0)
print(graph)
print(graph[n - 1][m - 1])
