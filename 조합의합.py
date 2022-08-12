candidates = [2, 3, 6, 7]
target = 7


def solution(candidates, target):
    result = []

    def dfs(nums, index):
        if sum(nums) == target:
            result.append(nums)
        else:
            for i in range(index, len(candidates)):
                if sum(nums + [candidates[i]]) <= target:
                    dfs(nums + [candidates[i]], i)

    dfs([], 0)

    return result


print(solution(candidates, target))
