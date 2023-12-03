def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= 1

    answer = sorted(answer, key = lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2, 3, 4, 5, 6]))