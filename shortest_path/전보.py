import collections
import heapq
n, m, start = map(int, input().split())

graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

Q = []
heapq.heappush(Q, (0, start))
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[x]:
            alt = w + time
            heapq.heappush(Q, (alt, v))

print(dist)

