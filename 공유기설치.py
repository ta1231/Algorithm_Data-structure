# c개의 공유기를 n개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 작성하기
n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

# 기준은 gap이다. 즉 mid는 start(가장 작은 gap)과 end(가장 큰 gap)에서 최적의 값을 찾아간다.
# 조건(다음 집이 가장 최근 공유기를 설치한 집(value)에 mid를 더한 값보다 크면)을 만족하면
# 공유기를 설치하는 집(value)을 최신화하고, count(공유기의 수)를 증가시켜준다.
start = array[1] - array[0]
end = array[-1] - array[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            count += 1
            value = array[i]
    # 설치한 공유기의 수가 c보다 크면 start를 업데이트해준다.(mid의 값이 점점 커짐)
    if count >= c:
        start = mid + 1
        result = mid
    # 아니면 end를 업데이트 해준다.(mid의 값이 점점 작아짐)
    else:
        end = mid - 1

print(result)