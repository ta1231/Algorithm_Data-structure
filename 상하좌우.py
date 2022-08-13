import sys

d = {'R': [0, 1],
     'U': [-1, 0],
     'L': [0, -1],
     'D': [1, 0]}
n = int(sys.stdin.readline().rstrip())
plans = list(map(str, input().split()))

nx = 1
ny = 1

for plan in plans:
    if 1 <= nx + d[plan][0] <= n and 1 <= ny + d[plan][1] <= n:
        nx += d[plan][0]
        ny += d[plan][1]
    else:
        continue
print(nx, ny)
