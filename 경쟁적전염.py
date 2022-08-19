from collections import deque
n, k = map(int, input().split())
graph = []
data = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])
data.sort()
q = deque(data)
target_s, target_x, target_y = map(int, input().split())

while q:
    num, time, x, y = q.popleft()
    if time == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            q.append([num, time + 1, nx, ny])
            graph[nx][ny] = num
print(graph[target_x - 1][target_y - 1])
