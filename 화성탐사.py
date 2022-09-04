import heapq
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    n = int(input())

    graph = collections.defaultdict(list)
    dist = collections.defaultdict(int)
    for i in range(n):
        lst = list(map(int, input().split()))
        for j in range(n):
            graph[(i, j)] = lst[j]
    q = [(graph[(0, 0)], 0, 0)]
    while q:
        cost, x, y = heapq.heappop(q)
        if (x, y) not in dist:
            dist[(x, y)] = cost
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    tmp = graph[(nx, ny)] + cost
                    heapq.heappush(q, (tmp, nx, ny))
    print(dist[(n - 1, n - 1)])
