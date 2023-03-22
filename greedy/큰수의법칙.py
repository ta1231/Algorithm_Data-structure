n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

count = m // (k + 1)
last = m % (k + 1)

print(count*(k*first+second) + first * last)