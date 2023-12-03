nums = [-1, 0, 1, 2, -1, 4]

# def solution(nums):
#     result = []
#     nums.sort()
#     for i in range(len(nums) - 2):
#         left = i + 1
#         right = len(nums) - 1
#
#         while left < right:
#             if sum([nums[i], nums[left], nums[right]]) < 0:
#                 left += 1
#             elif sum([nums[i], nums[left], nums[right]]) > 0:
#                 right -= 1
#             else:
#                 if [nums[i], nums[left], nums[right]] not in result:
#                     result.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#
#     return result
#
# print(solution(nums))


def solution(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if sum([nums[i], nums[left], nums[right]]) < 0:
                left += 1
            elif sum([nums[i], nums[left], nums[right]]) > 0:
                right -= 1
            else:
                if [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

print(solution(nums))