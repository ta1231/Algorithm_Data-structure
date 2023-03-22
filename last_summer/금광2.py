t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(lst[i * m: i * m + m])

    for c in range(1, m):
        for r in range(n):
            if r == 0:
                left_up = 0
                left_down = d[r + 1][c - 1]
                left = d[r][c - 1]
            elif r == n - 1:
                left_down = 0
                left_up = d[r - 1][c - 1]
                left = d[r][c - 1]
            else:
                left_up = d[r - 1][c - 1]
                left = d[r][c - 1]
                left_down = d[r + 1][c - 1]

            d[r][c] = d[r][c] + max(left_up, left, left_down)
    answer = 0
    for i in range(n):
        answer = max(d[i][m - 1], answer)
    print(answer)
