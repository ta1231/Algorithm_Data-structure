data = list(map(int, input()))
answer = 0

for i in data:
    if i == 0 or i == 1 or answer == 0:
        answer += i
    else:
        answer *= i
print(answer)