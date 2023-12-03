# from itertools import combinations
#
# n, m = map(int, input().split())
#
# grid = []
# house = []
# chicken = []
#
# answer = 10000
# for _ in range(n):
#     lst = list(map(int, input().split()))
#     grid.append(lst)
#
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 1:  # 1은 집
#             house.append([i, j])
#         elif grid[i][j] == 2:
#             chicken.append([i, j])  # 2는 치킨집
# combi = list(combinations(chicken, m))
#
#
# def min_distance(house, chicken):
#     tmp = []
#     for hx, hy in house:
#         m = 99999
#         for cx, cy in chicken:
#             m = min(m, abs(hx - cx) + abs(hy - cy))
#         tmp.append(m)
#     return sum(tmp)
#
#
# for c in combi:
#     answer = min(answer, min_distance(house, c))
# print(answer)

# from itertools import combinations
#
# n, m = map(int, input().split())
#
# grid = []
# house = []
# chicken = []
#
# for _ in range(n):
#     grid.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 1:  # 집
#             house.append([i, j])
#         elif grid[i][j] == 2:  # 치킨
#             chicken.append([i, j])
#
#
# def min_distance(house, comb):
#     tmp = []  # 각 집마다 comb중 가장 가까운거 저장
#     for hx, hy in house:
#         m = 99999
#         for cx, cy in comb:
#             m = min(m, abs(cx - hx) + abs(cy - hy))
#         tmp.append(m)
#
#     return sum(tmp)
#
#
# cc = combinations(chicken, m)
# answer = 99999
# for c in cc:
#     answer = min(answer, min_distance(house, c))
# print(answer)

from itertools import combinations

n, m = map(int, input().split())

grid = []
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            house.append([i, j])
        elif grid[i][j] == 2:
            chicken.append([i, j])

def min_distance(house, comb):
    tmp = []
    for hx, hy in house:
        m = 99999
        for cx, cy in comb:
            m = min(m, abs(cx - hx) + abs(cy - hy))
        tmp.append(m)
    return sum(m)


cc = combinations(chicken, m)
answer = 99999
for c in cc:
    answer = min(answer, min_distance(house, c))

print(answer)