hash_map = {')': '('}

def balanced_index(strs):
    count = 0
    for i, s in enumerate(strs):
        if s == '(':
            count += 1
        else:
            count -= 1
            if count == 0:
                return i

    return False


def collect(strs):
    stack = []
    for s in strs:
        if s not in hash_map:
            stack.append(s)
        elif not stack or stack.pop() != hash_map[s]:
            return False

    return len(stack) == 0



def solution(p):
    # step 1
    answer = ''
    if p == '':
        return ''
    # step 2
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # step 3
    if collect(u):
        answer = u + solution(v)
    # step 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i, tmp in enumerate(u):
            if tmp == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer

print(solution('()()())'))