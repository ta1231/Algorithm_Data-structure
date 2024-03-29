key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate_matrix(key: list) -> list:
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = key[i][j]
    return result


def check(new_lock):
    for i in range(len(new_lock) // 3, len(new_lock) // 3 * 2):
        for j in range(len(new_lock) // 3, len(new_lock) // 3 * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0] * 3 * m for _ in range(3 * m)]
    for i in range(m):
        for j in range(m):
            new_lock[m + i][m + j] = lock[i][j]

    for _ in range(4):
        key = rotate_matrix(key)
        for i in range(m * 2):
            for j in range(m * 2):
                for x in range(n):
                    for y in range(n):
                        new_lock[i + x][j + y] += key[x][y]
                if check(new_lock):
                    return True
                else:
                    for x in range(n):
                        for y in range(n):
                            new_lock[i + x][j + y] -= key[x][y]
    return False


print(solution(key, lock))



def rotate_matrix(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = key[i][j]
    return result

def check(new_lock):
    for i in range(len(new_lock) // 3, len(new_lock) // 3 * 2):
        for j in range(len(new_lock) // 3, len(new_lock) // 3 * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(m):
        for j in range(m):
            new_lock[m + i][m + j] = lock[i][j]
    for _ in range(4):
        key = rotate_matrix(key)
        for i in range(n * 2):
            for j in range(n * 2):
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += key[x][y]
                if check(new_lock):
                    return True
                else:
                    for x in range(m):
                        for y in range(m):
                            new_lock[i + x][j + y] -= key[x][y]
    return False


print(solution(key, lock))
