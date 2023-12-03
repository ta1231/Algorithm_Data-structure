# import collections
# import heapq
#
# n, m = map(int, input().split())
# start = int(input())
# graph = collections.defaultdict(list)
# dist = collections.defaultdict(int)
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# Q = []
# heapq.heappush(Q, (0, start))
# while Q:
#     time, node = heapq.heappop(Q)
#     if node not in dist:
#         dist[node] = time
#         for v, w in graph[node]:
#             alt = time + w
#             heapq.heappush(Q, (alt, v))
# print(dist)

# import collections
# import heapq
#
# n, m = map(int, input().split())
# start = int(input())
# graph = collections.defaultdict(list)
# dist = collections.defaultdict(int)
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# Q = []
# heapq.heappush(Q, (0, start))
#
# while Q:
#     time, node = heapq.heappop(Q)
#     if node not in dist:
#         dist[node] = time
#         for v, w in graph[node]:
#             alt = w + time
#             heapq.heappush(Q, (alt, v))
#
# print(dist)

# import heapq
# import collections
#
# graph = collections.defaultdict(list)
# dist = collections.defaultdict(int)
# n, m = map(int, input().split())
# start = int(input())
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])
#
# Q = []
# heapq.heappush(Q, (0, start))
# while Q:
#     time, node = heapq.heappop(Q)
#     if node not in dist:
#         dist[node] = time
#         for v, w in graph[node]:
#             alt = time + v
#             heapq.heappush(Q, (alt, w))
# print(dist)


import heapq
import collections

graph = collections.defaultdict(list)
dist = collections.defaultdict(int)
n, m = map(int, input().split())
start = int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

q = [(0, start)]

while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + v
            heapq.heappush(q, (alt, w))

print(dist)