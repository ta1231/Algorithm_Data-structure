# import heapq
# from collections import defaultdict
#
# n, m, k, x = map(int, input().split())
# graph = defaultdict(list)
# dist = defaultdict(int)
# q = []
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append([b, 1])
#
# q = [[0, x]]
#
# while q:
#     time, node = heapq.heappop(q)
#     if node not in dist:
#         dist[node] = time
#         for v, w in graph[node]:
#             alt = time + w
#             heapq.heappush(q, [alt, v])
#
# answer = []
#
# for d in dist:
#     if dist[d] == k:
#         answer.append(d)
#
# if answer:
#     for a in answer:
#         print(a)
# else:
#     print(-1)


import heapq
from collections import defaultdict

n, m, k, x = map(int, input().split())

dist = defaultdict(int)
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

q = [(0, x)]
while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(q, (alt, v))

answer = []
for d in dist:
    if dist[d] == k:
        answer.append(d)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)