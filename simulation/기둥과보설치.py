build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]


def solution(build_frame):
    house = []
    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            if [x, y, a] in house:
                house.remove([x, y, a])
            else:
                continue
        else:  # 설치

            if a == 0:  # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나 다른 기둥 위에 있어야 합니다.
                if y == 0 or [x, y - 1, 0] in house or [x - 1, y, 1] in house or [x, y, 1] in house:
                    house.append([x, y, 0])
                else:
                    continue
            else:  # 보는 한쪽 끝 부분이 기둥 위에 있더나 또는 양쪽 끝 부분이 다른 보와 동시에 연결 되어 있어야 합니다
                if [x + 1, y - 1, 0] in house or [x, y - 1, 0] in house or ([x - 1, y, 1] and [x + 1, y, 1]):
                    house.append([x, y, 1])
                else:
                    continue
        house.sort()
    return house


print(solution(build_frame))
