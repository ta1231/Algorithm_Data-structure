import re


def solution(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


print(solution('asa:'))
