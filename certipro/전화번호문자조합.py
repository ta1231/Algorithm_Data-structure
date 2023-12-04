dic = {"2": "abc",
       "3": "def",
       "4": "ghi",
       "5": "jkl",
       "6": "mno",
       "7": "pqrs",
       "8": "tuv",
       "9": "wxyz"}
digits = "23"


# def letterCombinations(digits):
#     def dfs(index, path):
#         if len(path) == len(digits):
#             result.append(path)
#             return
#         for i in range(index, len(digits)):
#             for j in dic[digits[i]]:
#                 dfs(i + 1, path + j)
#
#     if not digits:
#         return []
#
#     result = []
#
#     dfs(0, "")
#
#     return result
#
#
# print(letterCombinations(digits))

# def solution(digits):
#     def dfs(index, path):
#         if len(path) == len(digits):
#             result.append(path)
#             return
#         for i in range(index, len(digits)):
#             for j in dic[digits[i]]:
#                 dfs(i + 1, path + j)
#
#     if not digits:
#         return []
#
#     result = []
#
#     dfs(0, "")
#
#     return result
#
#
# print(solution(digits))


def solution(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)
    result = []

    dfs(0, "")

    return result

print(solution(digits))