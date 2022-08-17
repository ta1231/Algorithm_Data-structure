import copy
from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
time = [0] * (v + 1)

for i in range(1, v + 1):
    array = list(map(int, input().split()))
    time[i] = array[0]
    for a in array[1:-1]:
        indegree[i] += 1
        graph[a].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], time[i] + result[now])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result


print(topology_sort())
