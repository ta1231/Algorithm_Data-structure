s = 'aabbacc'

def solution(s):
    result = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        count = 1
        prev = s[:step]
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev

        result = min(result, len(compressed))
    return result

print(solution(s))