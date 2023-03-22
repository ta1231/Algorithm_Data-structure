n, m = map(int, input().split())

array = list(map(int, input().split()))

result = 0

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in array:
        if i > mid:
            tmp += i - mid
    if tmp >= m:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1

print(result)