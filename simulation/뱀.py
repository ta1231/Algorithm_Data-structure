n = int(input())
k = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

grid = [[0] * n for _ in range(n)]
snake = [[0, 0]]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 2

l = int(input())
tmp = 0
moves = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    moves.append([x - tmp, c])
    tmp = x
moves.append([100, 'C'])


def check(nx, ny):
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid) or grid[nx][ny] == 1:
        return False
    else:
        return True


def solution(moves):
    answer = 0
    direction = 0
    for x, c in moves:
        for _ in range(x):
            answer += 1
            nx = snake[-1][0] + dx[direction]
            ny = snake[-1][1] + dy[direction]
            if check(nx, ny):
                snake.append([nx, ny])
                if grid[nx][ny] == 2:
                    continue
                else:
                    px, py = snake.pop(0)
                    grid[px][py] = 0
                grid[nx][ny] = 1
            else:
                return answer

        if c == 'L':
            direction = (direction + 4 - 1) % 4
        elif c == 'D':
            direction = (direction + 4 + 1) % 4
        else:
            continue


print(solution(moves))
