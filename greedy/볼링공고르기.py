import collections
n, m = map(int, input().split())

balls = list(map(int, input().split()))
balls.sort()
answer = 0

count = collections.Counter(balls)

for i in range(1, m + 1):
    n -= count[i]
    answer += count[i] * n

print(answer)
