def solution(S):
    hash_map = {']': '[',
                '}': '{',
                ')': '('}

    stack = []
    flag = False

    for i, s in enumerate(S):
        if s == '/':
            if flag:
                flag = False
            else:
                flag = True
        if flag == False:
            if s == '/':
                continue
            if s not in hash_map:  # (, {, [, */인 경우
                stack.append(s)
            elif not stack or stack.pop() != hash_map[s]:
                print(stack)
                return 'FALSE'

    if len(stack) == 0:
        return 'TRUE'
    else:
        return 'FALSE'

print(solution("((/**/)(/**/)"))