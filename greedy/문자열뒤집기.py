lst = list(map(int, input()))
one = 0
zero = 0
count = 0
if lst[0] == 0:
    one += 1
else:
    zero += 1

for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:
        if lst[i] == 0:
            zero += 1
        else:
            one += 1

print(min(zero, one))

