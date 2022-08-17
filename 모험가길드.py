n = int(input())
lst = list(map(int, input().split()))
answer = 0
lst.sort()
count = 0
for f in lst:
    count += 1
    if count >= f:
        answer += 1
        count = 0
print(answer)