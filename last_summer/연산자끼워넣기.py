import sys
n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_value = sys.maxsize
max_value = -sys.maxsize
def dfs(i, now):
    global add, sub, mul, div, min_value, max_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - A[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * A[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / A[i]))
            div += 1
dfs(1, A[0])
print(min_value)
print(max_value)