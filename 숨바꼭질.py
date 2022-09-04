import heapq
import collections
n, m = map(int, input().split())
start = 1
graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([1, b])
    graph[b].append([1, a])

q = []
heapq.heappush(q, [0, 1])
while q:
    cost, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = cost
        for v, w in graph[node]:
            tmp = v + cost
            heapq.heappush(q, [tmp, w])

print(dist)
max_distance = 0
max_node = 0
result = []
for i in range(1, n + 1):
    if max_distance < dist[i]:
        max_node = i
        max_distance = dist[i]
        result = [max_node]
    elif max_distance == dist[i]:
        result.append(i)
print(max_node, max_distance, len(result))
