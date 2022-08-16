n, m = map(int, input().split())


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


parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
array = []
for _ in range(m):
    a, b, c = map(int, input().split())
    array.append((c, a, b))
array.sort()
count = 0
last = 0
for c, a, b in array:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        count += c
        last = c

    else:
        continue
print(count - last)
