def solution(n, k):
    result = []
    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    dfs([], 1, k)
    return result

print(solution(4, 2))