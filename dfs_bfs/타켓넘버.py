def solution(numbers, target):
    lst = []
    def dfs(numbers, target, depth):
        if depth == len(numbers):
            if sum(numbers) == target:
                lst.append(1)
            else:
                return
        else:
            dfs(numbers, target, depth + 1)
            numbers[depth] *= -1
            dfs(numbers, target, depth + 1)
    dfs(numbers, target, 0)
    return len(lst)

print(solution([1, 1, 1, 1, 1], 3))