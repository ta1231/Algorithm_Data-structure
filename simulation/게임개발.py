
# n, m = map(int, input().split())
#
# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
#
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 x좌표, y좌표 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else:
#             break
#         turn_time = 0
#
# print(count)


n, m = map(int, input().split())
r, c, d = map(int, input().split())

direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
rotate = {1: 0, 2: 1, 3: 2, 0: 3}
answer = 1
grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))
grid[r][c] = 2
while True:
    # 현재 위치에서 현재 방향을 기준으로 왼쪽으로 돈다
    d = rotate[d]
    # 만약 그 방향으로 간적이 없다면 간다
    if grid[r + direction[d][0]][c + direction[d][1]] == 0:
        r = r + direction[d][0]
        c = c + direction[d][1]
        grid[r][c] = 2
        answer += 1
    else:
        if grid[r - 1][c] != 0 and grid[r + 1][c] != 0 and grid[r][c - 1] != 0 and grid[r][c + 1] != 0:
            if grid[r - direction[d][0]][c - direction[d][1]] == 1:
                break
            else:
                r = r - direction[d][0]
                c = c - direction[d][1]
                grid[r][c] = 2

print(answer)

