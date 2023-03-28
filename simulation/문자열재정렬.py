inp = input()
digit = []
string = []
for i in inp:
    if i.isdigit():
        digit.append(int(i))
    else:
        string.append(i)
print(digit)
print(''.join(sorted(string)) + str(sum(digit)))

