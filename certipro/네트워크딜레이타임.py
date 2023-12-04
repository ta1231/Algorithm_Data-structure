import heapq
from collections import defaultdict


# def iterative_dfs(start_v):
#     discovered = [start_v]
#     queue = [start_v]
#
#     while queue:
#         v = queue.pop(0)
#         for w in graph[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 queue.append(w)
#     return discovered


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2


# def solution(times, n, k):
#     dic = defaultdict(list)
#     for u, v, w in times:
#         dic[u].append((v, w))
#     Q = [(0, k)]  # time, node
#     dist = defaultdict(int)
#
#     while Q:
#         time, node = heapq.heappop(Q)
#         if node not in dist:
#             dist[node] = time
#             for v, w in dic[node]:
#                 alt = time + w
#                 heapq.heappush(Q, (alt, v))
#     if len(dist) == n:
#         return max(dist.values())
#     return -1
#
#
# print(solution(times, n, k))

# def solution(times, n, k):
#     dic = defaultdict(list)
#     for u, v, w in times:
#         dic[u].append((v, w))
#     Q = [(0, k)]
#     dist = defaultdict(int)
#
#     while Q:
#         time, node = heapq.heappop(Q)
#         if node not in dist:
#             dist[node] = time
#             for v, w in dic[node]:
#                 alt = time + w
#                 heapq.heappush(Q, (alt, v))
#     if len(dist) == n:
#         return max(dist.values())
#     return -1


# def solution(times, n, k):
#     dic = defaultdict(list)
#     for u, v, w in times:
#         dic[u].append((v, w))
#     Q = [(0, k)]
#     dist = defaultdict(int)
#
#     while Q:
#         time, node = heapq.heappop(Q)
#         if node not in dist:
#             dist[node] = time
#             for v, w in dic[node]:
#                 alt = time + w
#                 heapq.heappush(Q, (alt, v))
#     if len(dist) == n:
#         return max(dist.values())
#     return -1
#
# print(solution(times, n, k))


def solution(times, n, k):
    dic = defaultdict(list)
    for u, v, w in times:
        dic[u].append((v, w))
    dist = defaultdict(int)
    Q = [(0, k)]
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in dic[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == n:
        return max(dist.values())
    return -1

print(solution(times, n, k))