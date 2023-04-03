n, k = map(int, input().split())

grid = []
virus = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(n):
        if grid[i][j] != 0:
            virus.append([grid[i][j], i, j])

s, x, y = map(int, input().split())

q = sorted(virus)
for i in q:
    i.append(s)

while q:
    v, vx, vy, s = q.pop(0)
    if s == 0:
        break

    grid[vx][vy] = v
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            q.append([v, nx, ny, s - 1])

print(grid[x - 1][y - 1])