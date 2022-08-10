# 이 문제의 기본 아이디어는 '가장 긴 증가하는 부분 수열'로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같음
# 모든 0 <= j , i에 대하여 dp[i] = max(dp[i], dp[j] + 1) if array[j] < array[i]
# n = int(input())
# array = list(map(int, input().split()))
# array.reverse()
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(n - max(dp))

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(n - max(dp))
