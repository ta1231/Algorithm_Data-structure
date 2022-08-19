import itertools

n, m = map(int, input().split())
graph = []
home = []
chicken = []
# 0은 빈칸, 1은 집, 2는 치킨집
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

cc = list(itertools.combinations(chicken, 3))


def min_distance(house, chicken):
    hlst = []
    for h in house:
        htmp = 999
        for c in chicken:
            htmp = min(htmp, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        hlst.append(htmp)
    return sum(hlst)


answer = 999

for c in cc:
    answer = min(answer, min_distance(home, c))
print(answer)