n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[5] = 1
for i in range(2, 1001):
    if dp[i] == 1:
        continue
    else:
        if (i % 2 == 0 and dp[i // 2] == 1) or (i % 3 == 0 and dp[i // 3] == 1) or (i % 5 == 0 and dp[i // 5] == 1):
            dp[i] = 1
count = 0
for number in range(1, 1001):
    if dp[number] == 1:
        count += 1
    else:
        continue
    if count == n:
        print(number)
        break

