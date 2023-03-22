n, m = map(int, input().split())
nx, ny, d = map(int, input().split())

direction = {0: [-1, 0],
             1: [0, 1],
             2: [1, 0],
             3: [0, -1]}
rotate = {0: 3,
          3: 2,
          2: 1,
          1: 0}

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
count = 1
graph[nx][ny] = 2
while True:

    if graph[nx + direction[rotate[d]][0]][ny + direction[rotate[d]][1]] == 0:
        nx += direction[rotate[d]][0]
        ny += direction[rotate[d]][1]
        d = rotate[d]
        graph[nx][ny] = 2
        count += 1
    else:
        d = rotate[d]

    if graph[nx + direction[0][0]][ny + direction[0][1]] != 0 and graph[nx + direction[1][0]][ny + direction[1][1]] != 0 and graph[nx + direction[2][0]][ny + direction[2][1]] != 0 and graph[nx + direction[3][0]][ny + direction[3][1]] != 0:
        if graph[nx - direction[d][0]][ny - direction[d][1]] == 1:
            break
        else:
            nx -= direction[d][0]
            ny -= direction[d][1]
print(count)
