from collections import deque

n, l, r = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def process(i, j, index):
    united = []
    q = deque()
    q.append((i, j))
    united.append((i, j))
    union[i][j] = index
    summary = graph[i][j]
    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    summary += graph[nx][ny]
                    united.append((nx, ny))
                    union[nx][ny] = index

    for tx, ty in united:
        graph[tx][ty] = summary // count

answer = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    answer += 1

print(answer)