n = int(input())
t = []  # 각 상담을 완료하는 데 걸리는 기간
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(dp)
