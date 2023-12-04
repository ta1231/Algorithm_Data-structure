import collections

tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]


# def solution(tickets):
#     path = []
#     routes = collections.defaultdict(list)
#     for start, destination in tickets:
#         routes[start].append(destination)
#
#     for start in routes:
#         routes[start].sort()
#
#     def dfs(a):
#         while routes[a]:
#             dfs(routes[a].pop(0))
#         path.append(a)
#
#     dfs('JFK')
#
#     return path[::-1]
#
# print(solution(tickets1))
# print(solution(tickets2))


def solution(tickets):
    path = []
    routes = collections.defaultdict(list)
    for start, destination in tickets:
        routes[start].append(destination)

    for start in routes:
        routes[start].sort()

    def dfs(a):
        while routes[a]:
            dfs(routes[a].pop(0))
        path.append(a)

    dfs('JFK')

    return path[::-1]


print(solution(tickets1))
print(solution(tickets2))
