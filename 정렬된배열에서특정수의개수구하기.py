# 조건: o(logN)으로 알고리즘 설계하기
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)