n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]


def solution(n, results):
    INF = 1e9
    grid = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        grid[i][i] = 0

    for a, b in results:
        grid[a][b] = 1

    for k in range(n + 1):
        for a in range(n + 1):
            for b in range(n + 1):
                grid[a][b] = min(grid[a][b], grid[a][k] + grid[k][b])

    answer = 0

    for i in range(n + 1):
        count = 0
        for j in range(n + 1):
            if grid[i][j] != INF or grid[j][i] != INF:
                count += 1
        if count == n:
            answer += 1
    return answer
