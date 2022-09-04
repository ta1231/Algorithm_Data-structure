n = int(input())
dp = [0] * 1000
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[5] = 1
count = 1
for i in range(2, 1000):
    if dp[i] == 1:
        count += 1
    if dp[i] == 0:
        if (i % 2 == 0 and dp[i // 2] == 1) or (i % 3 == 0 and dp[i // 3] == 1) or (i % 5 == 0 and dp[i // 5] == 1):
            dp[i] = 1
            count += 1
            if count == n:
                print(i)
                break
