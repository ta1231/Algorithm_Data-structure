inp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


# def solution(heights):
#     left = 0
#     right = len(heights) - 1
#     max_left = heights[left]
#     max_right = heights[right]
#     answer = 0
#
#     while left < right:
#         max_left = max(heights[left], max_left)
#         max_right = max(heights[right], max_right)
#
#         if max_left <= max_right:
#             answer += max_left - heights[left]
#             left += 1
#         else:
#             answer += max_right - heights[right]
#             right -= 1
#
#     return answer
#
# print(solution(inp))

def solution(heights):
    left = 0
    right = len(heights) - 1
    max_left = heights[left]
    max_right = heights[right]
    answer = 0

    while left < right:
        max_left = max(heights[left], max_left)
        max_right = max(heights[right], max_right)

        if max_left < max_right:
            answer += max_left - heights[left]
            left += 1
        else:
            answer += max_right - heights[right]
            right -= 1
    return answer

print(solution(inp))
