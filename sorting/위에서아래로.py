n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
print(sorted(lst, reverse=True))