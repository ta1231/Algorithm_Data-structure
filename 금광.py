t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m

    # 1. 2열부터는 각 자리에서의 최대값이 무엇인지 구해줘야한다.
    # 2. left_up, left, left_down의 최대값과 현재 값을 합쳐 update해줘야한다.
    # 3. 맨 마지막 열에서 가장 큰 값이 답이된다.

    # 1번
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            # 2번
            dp[i][j] = dp[i][j] + max(left, left_up, left_down)

    # 3번
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
