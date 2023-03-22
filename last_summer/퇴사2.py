n = int(input())
time = []
price = []
dp = [0] * (n + 1)

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)
answer = 0
for i in range(n - 1, -1, -1):
    tmp = time[i] + i
    if tmp > n:
        dp[i] = answer
    else:
        answer = max(answer, dp[tmp] + price[i])
        dp[i] = answer
print(answer)
print(dp)