def solution(inp):
    table = {')': '(',
             '}': '{',
             ']': '['}
    stack = []
    for char in inp:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0