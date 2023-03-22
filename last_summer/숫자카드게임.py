n, m = map(int, input().split())
result = 0
for _ in range(n):
    tmp = min(list(map(int, input().split())))
    result = max(tmp, result)

print(result)