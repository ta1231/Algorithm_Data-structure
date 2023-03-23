n = int(input())
parts = set(map(int, input().split()))
m = map(int, input())
find = list(map(int, input().split()))

for i in find:
    if i in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')
