from pprint import pprint

n, m = map(int, input().split())

grid = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    grid.append(list(map(int, input())))

discovered = [[0, 0]]
queue = [[0, 0]]
while queue:
    v = queue.pop(0)
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1:
                grid[nx][ny] = grid[v[0]][v[1]] + 1
                queue.append([nx, ny])

pprint(grid[n - 1][m - 1])
pprint(grid)