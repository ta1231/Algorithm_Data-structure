import itertools
import copy

n, m = map(int, input().split())
graph = []
virus = []
vac = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            vac.append([i, j])
        elif graph[i][j] == 2:
            virus.append([i, j])
        else:
            continue


def count_safe(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


cc = list(itertools.combinations(vac, 3))

answer = 0
for c in cc:
    graph_ = copy.deepcopy(graph)
    graph_[c[0][0]][c[0][1]] = 1
    graph_[c[1][0]][c[1][1]] = 1
    graph_[c[2][0]][c[2][1]] = 1
    q = copy.deepcopy(virus)
    while q:
        x, y = q.pop(0)
        graph_[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph_[nx][ny] == 0:
                q.append([nx, ny])

    answer = max(answer, count_safe(graph_))

print(answer)
