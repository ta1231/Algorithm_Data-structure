import itertools
import copy

n = int(input())
graph = []
teacher = []
student = 0
dis = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == 'X':
            dis.append([i, j])
        if graph[i][j] == 'S':
            student += 1
        if graph[i][j] == 'T':
            teacher.append([i, j])


def counter():
    count = 0
    for i in range(n):
        for j in range(n):
            if graph_[i][j] == 'S':
                count += 1
    if count == student:
        return True
    else:
        return False


def dfs(i, j, d):
    graph_[i][j] = 'T'
    nx = i + dx[d]
    ny = j + dy[d]

    if 0 <= nx < n and 0 <= ny < n and graph_[nx][ny] != 'O':
        dfs(nx, ny, d)


cc = list(itertools.combinations(dis, 3))
answer = 'NO'
for c in cc:
    graph_ = copy.deepcopy(graph)
    graph_[c[0][0]][c[0][1]] = 'O'
    graph_[c[1][0]][c[1][1]] = 'O'
    graph_[c[2][0]][c[2][1]] = 'O'

    for tx, ty in teacher:
        for i in range(4):
            dfs(tx, ty, i)
    if counter():
        answer = 'YES'
print(answer)
