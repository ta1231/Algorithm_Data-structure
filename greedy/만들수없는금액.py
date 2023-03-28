### 내풀이 ###

# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort(reverse=True)
#
# answer = 0
#
# while True:
#     answer += 1
#     tmp = answer
#     for coin in coins:
#         if tmp - coin < 0:
#             continue
#         else:
#             tmp -= coin
#
#     if tmp != 0:
#         break
#
# print(answer)


### 답지 ###

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
    if target < i:
        break
    target += i

print(target)