n = int(input())
lst = []
for _ in range(n):
    name, score = map(str, input().split())
    score = int(score)
    lst.append([name, score])
for i in sorted(lst, key=lambda x: x[1]):
    print(i[0], end=' ')
