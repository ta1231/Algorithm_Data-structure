def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i, cur in enumerate(prices):
        while stack and cur < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    while stack:
        i = stack.pop()
        answer[i] = len(prices) - 1 - i
    return answer

print(solution([1, 2, 3, 2, 3]))