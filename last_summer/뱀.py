n = int(input())
k = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
l = int(input())
body = []
nx, ny = 0, 0
body.append([nx, ny])
time = 0
move = []
for _ in range(l):
    x, c = map(str, input().split())
    x = int(x)
    move.append([x - time, c])
    time = x
move.append([100, 'C'])
def solution(nx, ny):
    answer = 0
    d = 0

    for x, c in move:
        for _ in range(x):
            if 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < n and [nx + dx[d], ny + dy[d]] not in body:
                nx += dx[d]
                ny += dy[d]
                body.append([nx, ny])
                answer += 1
                if board[nx][ny] != 1:
                    body.pop(0)
                board[nx][ny] = 0

            else:
                return answer + 1
        if c == 'L':
            d = (d + 4 - 1) % 4
        elif c == 'D':
            d = (d + 4 + 1) % 4
        else:
            continue
print(solution(nx, ny))