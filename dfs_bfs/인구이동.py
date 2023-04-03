# n, l, r = map(int, input().split())
# grid = []
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# for _ in range(n):
#     grid.append(list(map(int, input().split())))
#
#
# def process(i, j, index):
#     united = []
#     q = [[i, j]]
#     united.append([i, j])
#     union[i][j] = index
#     count = 1
#     summary = grid[i][j]
#     while q:
#         x, y = q.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(grid[nx][ny] - grid[x][y]) <= r:
#                     summary += grid[nx][ny]
#                     union[nx][ny] = index
#                     united.append([nx, ny])
#                     q.append([nx, ny])
#                     count += 1
#
#     for x, y in united:
#         grid[x][y] = summary // count
#
#
# answer = 0
#
# while True:
#     union = [[-1] * n for _ in range(n)]
#     index = 0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process(i, j, index)
#                 index += 1
#     if index == n * n:
#         break
#     answer += 1
#
# print(answer)


n, l, r = map(int, input().split())
grid = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(n):
    grid.append(list(map(int, input().split())))


def process(i, j, index):
    q = [[i, j]]
    united = [[i, j]]
    summary = grid[i][j]
    count = 1
    union[i][j] = index

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(grid[x][y] - grid[nx][ny]) <= r:
                    q.append([nx, ny])
                    united.append([nx, ny])
                    summary += grid[nx][ny]
                    union[nx][ny] = index
                    count += 1

    for x, y in united:
        grid[x][y] = summary // count


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
