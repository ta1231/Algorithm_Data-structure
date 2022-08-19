inp = list(map(int, input()))
length = len(inp)
if sum(inp[:length // 2]) == sum(inp[length // 2:]):
    print('LUCKY')
else:
    print('READY')