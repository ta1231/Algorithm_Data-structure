n = int(input())
array = list(map(int, input().split()))
m = int(input())
needs = list(map(int, input().split()))

array.sort()


def binary_search(array, need, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == need:
            return 'yes'
        elif array[mid] > need:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

for need in needs:
    print(binary_search(array, need, 0, n - 1), end=' ')
