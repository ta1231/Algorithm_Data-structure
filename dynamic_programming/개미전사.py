n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = lst[0]
# dp[1] = lst[1]
dp[1] = max(lst[0], lst[1])
for i in range(2, n):
    dp[i] = max(lst[i] + dp[i - 2], dp[i - 1])
print(max(dp))
