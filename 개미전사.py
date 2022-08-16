n = int(input())
array = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = array[0]
dp[1] = array[1]
for i in range(2, n):
    dp[i] = max(array[i] + dp[i - 2], dp[i - 1])
print(dp[n - 1])
