lst = list(map(int, input()))
answer = lst.pop(0)

for i in lst:
    if answer == 0:
        answer += i
    else:
        if i <= 1:
            answer += i
        else:
            answer *= i

print(answer)
