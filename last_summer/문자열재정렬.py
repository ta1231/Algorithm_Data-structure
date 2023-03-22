inp = input()
digit = []
strs = []
for i in inp:
    if i.isdigit():
        digit.append(i)
    else:
        strs.append(i)

print(''.join(sorted(strs)) + ''.join(''.join(sorted(digit))))