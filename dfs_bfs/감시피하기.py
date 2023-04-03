from itertools import combinations
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
S = []
T = []
X = []
grid = []
students = 0
count_list = []
for i in range(n):
    grid.append(list(input().split()))
    for j in range(n):
        if grid[i][j] == 'X':
            X.append([i, j])
        elif grid[i][j] == 'T':
            T.append([i, j])
        else:
            S.append([i, j])
            students += 1


def count_student(new_grid):
    count = 0
    for i in range(n):
        for j in range(n):
            if new_grid[i][j] == 'S':
                count += 1
    return count

def dfs(x, y, direction):
    new_grid[x][y] = 'T'
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n and new_grid[nx][ny] != 'W':
        dfs(nx, ny, direction)


cc = combinations(X, 3)


for c in cc:
    new_grid = copy.deepcopy(grid)
    new_grid[c[0][0]][c[0][1]] = 'W'
    new_grid[c[1][0]][c[1][1]] = 'W'
    new_grid[c[2][0]][c[2][1]] = 'W'

    for tx, ty in T:
        for i in range(4):
            dfs(tx, ty, i)

    count_list.append(count_student(new_grid))

if students in count_list:
    print('YES')
else:
    print('NO')
