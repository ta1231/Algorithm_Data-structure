n, m = map(int, input().split())
grid = []
answer = 0
for _ in range(n):
    grid.append(list(input()))


def dfs(i, j):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1 or grid[i][j] == '1':
        return
    grid[i][j] = '1'

    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)


for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            dfs(i, j)
            answer += 1
print(answer)
