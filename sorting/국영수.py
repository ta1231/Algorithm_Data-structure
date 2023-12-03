# (정렬) 국영수

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(str, input().split())))
    lst[-1][1] = int(lst[-1][1])
    lst[-1][2] = int(lst[-1][2])
    lst[-1][3] = int(lst[-1][3])

lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(lst[i][0])