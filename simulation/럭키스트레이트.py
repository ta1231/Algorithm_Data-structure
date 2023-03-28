lst = list(map(int, input()))
mid = len(lst) // 2
if sum(lst[:mid]) == sum(lst[mid:]):
    print('LUCKY')
else:
    print('READY')