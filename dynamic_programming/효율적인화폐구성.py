# n, m = map(int, input().split())
# coins = []
# dp = [10001] * (m + 1)
# dp[0] = 0
# for _ in range(n):
#     coins.append(int(input()))
#
# for i in range(n):
#     for j in range(coins[i], m + 1):
#         if dp[j - coins[i]] != 10001:
#             dp[j] = min(dp[j], dp[j - coins[i]] + 1)
#
# print(dp[m])
# print(dp)
n, m = map(int, input().split())
coins = []
dp = [10001] * (m + 1)
dp[0] = 0
for _ in range(n):
    coins.append(int(input()))

for i in range(n):
    for j in range(coins[i], m + 1):
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

print(dp[m])
print(dp)
