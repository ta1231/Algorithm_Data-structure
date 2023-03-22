n = int(input())
plans = list(map(str, input().split()))
x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            if 1 <= x + dx[i] < n and 1 <= y + dy[i] < n:
                x += dx[i]
                y += dy[i]
print(x, y)

