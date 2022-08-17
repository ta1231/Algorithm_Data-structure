import heapq

food_times = [3, 1, 2]
k = 5


def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_values = 0
    length = len(food_times)
    previous = 0
    while sum_values + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_values += (now - previous) * length
        length -= 1
        previous = now
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_values) % length][1]


print(solution(food_times, k))
