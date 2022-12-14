def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, n + 1):
        dp[0][i] = i
    for j in range(1, m + 1):
        dp[j][0] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = 1 + min(dp[j][i - 1], dp[j - 1][i], dp[j - 1][i - 1])
    return dp[m - 1][n - 1]


a = input()
b = input()

print(edit_distance(a, b))
