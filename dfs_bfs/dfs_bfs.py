graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


# def recursive_dfs(v, discovered = []):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = recursive_dfs(w, discovered)
#     return discovered
#
#
# print(recursive_dfs(1))

# def dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = dfs(w, discovered)
#     return discovered
#
#
# print(dfs(1))
#
#
# def iterative_bfs(start_v):
#     discovered = [start_v]
#     queue = [start_v]
#     while queue:
#         v = queue.pop(0)
#         for w in graph[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 queue.append(w)
#     return discovered
#
# print(iterative_bfs(1))


#
# def dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = dfs(w, discovered)
#     return discovered
#
# print(dfs(1))
#
# def bfs(start_v):
#     discovered = [start_v]
#     queue = [start_v]
#     while queue:
#         v = queue.pop(0)
#         for w in graph[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 queue.append(w)
#
#     return discovered
#
# print(bfs(1))


# def dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = dfs(w, discovered)
#
#     return discovered
#
#
# print(dfs(1))
#
#
# def bfs(start_v):
#     discovered = [start_v]
#     queue = [start_v]
#     while queue:
#         v = queue.pop(0)
#         for w in graph[v]:
#             if w not in discovered:
#                 queue.append(w)
#                 discovered.append(w)
#
#     return discovered
#
#
# print(bfs(1))


# def dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = dfs(w, discovered)
#
#     return discovered
#
#
# def bfs(start_v):
#     q = [start_v]
#     discovered = [start_v]
#     while q:
#         v = q.pop(0)
#         for w in graph[v]:
#             if w not in discovered:
#                 q.append(w)
#                 discovered.append(w)
#
#     return discovered
#
#
# print(dfs(1))
# print(bfs(1))

def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs(w, discovered)
    return discovered


def bfs(start_v):
    q = [start_v]
    discovered = [start_v]

    while q:
        v = q.pop(0)
        for w in graph[v]:
            if w not in discovered:
                q.append(w)
                discovered.append(w)
    return discovered

print(dfs(1))
print(bfs(1))