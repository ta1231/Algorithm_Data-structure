# 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.

n = int(input())
array = list(map(int, input().split()))

start = 0
end = n - 1
answer = -1
while start <= end:
    mid = (start + end) // 2
    if mid == array[mid]:
        answer = mid
        break
    elif mid < array[mid]:
        end = mid - 1
    else:
        start = mid + 1
print(answer)
