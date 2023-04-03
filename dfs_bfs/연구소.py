# from itertools import combinations
# import copy
#
# n, m = map(int, input().split())
# grid = []
# vac = []
# wall = []
# virus = []
#
# for i in range(n):
#     grid.append(list(map(int, input().split())))
#     for j in range(m):
#         if grid[i][j] == 0:
#             vac.append([i, j])
#         elif grid[i][j] == 2:
#             virus.append([i, j])
#         else:
#             continue
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
#
# answer = 0
#
#
# def count_safe(new_grid):
#     count = 0
#     for ii in range(n):
#         for ij in range(m):
#             if new_grid[ii][ij] == 0:
#                 count += 1
#     return count
#
#
# cc = list(combinations(vac, 3))
# for c in cc:
#     new_grid = copy.deepcopy(grid)
#     new_grid[c[0][0]][c[0][1]] = 1
#     new_grid[c[1][0]][c[1][1]] = 1
#     new_grid[c[2][0]][c[2][1]] = 1
#
#     q = copy.deepcopy(virus)
#
#     while q:
#         vx, vy = q.pop(0)
#         new_grid[vx][vy] = 2
#         for i in range(4):
#             nx = vx + dx[i]
#             ny = vy + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m and new_grid[nx][ny] == 0:
#                 q.append([nx, ny])
#
#     answer = max(answer, count_safe(new_grid))
#
# print(answer)
#


from itertools import combinations
import copy

n, m = map(int, input().split())

grid = []
vac = []
virus = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(m):
        if grid[i][j] == 0:
            vac.append([i, j])
        elif grid[i][j] == 2:
            virus.append([i, j])
        else:
            continue


def count_safe(new_grid):
    count = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if new_grid[i][j] == 0:
                count += 1

    return count


cc = combinations(vac, 3)
answer = 0
for c in cc:
    new_grid = copy.deepcopy(grid)
    new_grid[c[0][0]][c[0][1]] = 1
    new_grid[c[1][0]][c[1][1]] = 1
    new_grid[c[2][0]][c[2][1]] = 1

    q = copy.deepcopy(virus)
    while q:
        vx, vy = q.pop(0)
        new_grid[vx][vy] = 2
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_grid[nx][ny] == 0:
                q.append([nx, ny])

    answer = max(answer, count_safe(new_grid))

print(answer)
