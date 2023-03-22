n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] == 1:
        return
    graph[i][j] = 1

    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)


answer = 0
print(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            answer += 1
print(answer)
