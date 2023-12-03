# n, m = map(int, input().split())
#
# lst = list(map(int, input().split()))
#
# start = 0
# end = max(lst)
# answer = 0
# while start <= end:
#     mid = (start + end) // 2
#     tmp = 0
#     for cake in lst:
#         if cake > mid:
#             tmp += (cake - mid)
#     if tmp >= m:
#         answer = max(mid, answer)
#         start = mid + 1
#     else:
#         end = mid - 1
# print(answer)

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
#
# start = 0
# end = max(lst)
# answer = 0
# while start <= end:
#     mid = (start + end) // 2
#     tmp = 0
#     for cake in lst:
#         if cake > mid:
#             tmp += cake - mid
#     if tmp >= m:
#         answer = max(mid, answer)
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(answer)

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for cake in lst:
        if cake > mid:
            tmp += cake - mid
    if tmp > m:
        answer = max(mid, answer)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
