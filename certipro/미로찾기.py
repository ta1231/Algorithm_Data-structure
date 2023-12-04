# 입력예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
#
# 출력예시
# 10

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Q = [(0, 0)]
while Q:
    x, y = Q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            Q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
print(graph[n - 1][m - 1])
