n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10000] * (m + 1)
d[0] = 0
for coin in coins:
    if coin <= m:
        d[coin] = 1

for i in range(1, m + 1):
    for coin in coins:
        if (i - coin) >= 0:
            if d[i - coin] != 10000:
                d[i] = min(d[i], d[i - coin] + 1)
if d[m] == 10000:
    print('-1')
else:
    print(d[m])
