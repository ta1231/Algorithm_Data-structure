# def find_parent(parent, x):
#     # 루트노드가 아니라면 루트노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# v, e = map(int, input().split())
# parent = [0] * (v + 1)
#
# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i
#
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# # 각 원소가 속한 집합 출력
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')
#
# print()
#
# for i in range(1, v + 1):
#     print(parent[i], end=' ')


# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# v, e = map(int, input().split())
#
# parent = [0] * (v + 1)
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')
#
# print()
#
# for i in range(1, v + 1):
#     print(parent[i], end=' ')

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print(parent)