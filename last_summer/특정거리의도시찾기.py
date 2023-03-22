import collections
import heapq
n, m, k, x = map(int, input().split())

graph = collections.defaultdict(list)
dist = collections.defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

q = [(0, x)]
while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = w + time
            heapq.heappush(q, (alt, v))
answer = []
for node in dist:
    if dist[node] == k:
        answer.append(node)
if answer:
    for i in sorted(answer):
        print(i)
else:
    print(-1)