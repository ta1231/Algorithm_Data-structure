import re
from collections import Counter

paragraph = 'Bob hit a ball, the hit BALL flew Far after it was hit'

banned = ['hit']


def solution(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counter = Counter(words)
    return counter.most_common(1)[0][0]


print(solution(paragraph, banned))
