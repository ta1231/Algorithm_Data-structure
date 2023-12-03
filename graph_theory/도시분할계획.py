# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# n, m = map(int, input().split())
#
# edges = []
# result = 0
# parent = [0] * (n + 1)
# for i in range(1, n + 1):
#     parent[i] = i
#
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
# max_cost = 0
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         result += cost
#         union_parent(parent, a, b)
#         max_cost = max(cost, max_cost)
#
# print(result - max_cost)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * len(v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
result = 0
max_cost = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        max_cost = max(cost, max_cost)
print(result - cost)
