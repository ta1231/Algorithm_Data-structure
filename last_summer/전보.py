import collections
import heapq

n, m, start = map(int, input().split())
graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, start))

while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = w + time
            heapq.heappush(q, (alt, v))
first = len(dist) - 1
second = 0
for node in dist:
    second = max(dist[node], second)
print(dist)
print(first, second)
