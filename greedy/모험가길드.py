n = int(input())
lst = list(map(int, input().split()))

lst.sort()
count = 0
answer = 0

for i in lst:
    count += 1
    # i보다 count가 같거나 커야지 answer += 1, count += 1
    if count >= i:
        answer += 1
        count = 0
    else:
        continue

print(answer)
