import collections
import heapq

n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0


# def solution(n, edges, src, dst, K):
#     graph = collections.defaultdict(list)
#     for u, v, w in edges:
#         graph[u].append((v, w))
#     Q = [(0, src, K)]
#     while Q:
#         price, node, remains = heapq.heappop(Q)
#         if node == dst:
#             return price
#         if remains >= 0:
#             for v, w in graph[node]:
#                 alt = price + w
#                 heapq.heappush(Q, (alt, v, remains - 1))
#     return -1
#
#
# print(solution(n, edges, src, dst, K))


def solution(n, edges, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    Q = [(0, src, K)]
    while Q:
        price, node, remains = heapq.heappop(Q)
        if node == dst:
            return price
        if remains >= 0:
            for v, w in graph[node]:
                alt = w + price
                heapq.heappush(Q, (alt, v, remains - 1))

    return -1


print(solution(n, edges, src, dst, K))
