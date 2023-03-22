inp = input()

def balance(strs):
    open = 0
    close = 0
    for s in strs:
        if s == '(':
            open += 1
        else:
            close += 1
    return open == close

def collect(strs):
    table = {')': '('}
    stack = []
    for s in strs:
        if s not in table:
            stack.append(s)
        elif not stack or stack.pop() != table[s]:
            return False

    return len(stack) == 0

def solution(p):
    answer = ''
    if p == '':
        return ''
    for i in range(1, len(p) + 1):
        if balance(p[:i]):
            u = p[:i]
            v = p[i:]
    if collect(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for t in u:
            if t == '(':
                answer += ')'
            else:
                answer += '('
    return answer
print(solution(inp))