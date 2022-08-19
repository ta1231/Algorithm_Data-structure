def available(answer):
    for x, y, a in answer:
        # 기둥을 설치할 때
        if a == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보를 설치할 때
        elif a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 삭제한다면
        if b == 0:
            answer.remove([x, y, a])
            if not available(answer):
                answer.append([x, y, a])
        # 설치한다면
        if b == 1:
            answer.append([x, y, a])
            if not available(answer):
                answer.remove([x, y, a])
    return sorted(answer)
