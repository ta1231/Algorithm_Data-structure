import heapq
import collections

graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

n, m, k, x = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

Q = [(0, x)]
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))
answer = []
for node in dist:
    if dist[node] == k:
        answer.append(node)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)
