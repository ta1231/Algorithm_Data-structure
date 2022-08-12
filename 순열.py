# def recursive_dfs(v, discovered=[])
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = recursive_dfs(w, discovered)
#     return discovered

inp = [1, 2, 3]
def solution(inp):
    result = []
    tmp = []
    def dfs(elements):
        if len(tmp) == len(inp):
            result.append(tmp[:])
        for e in elements:
            tmp.append(e)
            next_elements = elements[:]
            next_elements.remove(e)
            dfs(next_elements)
            tmp.pop()
    dfs(inp)

    return result
print(solution(inp))
