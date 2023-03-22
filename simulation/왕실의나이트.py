input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

answer = 0

for step in steps:
    nx = row + step[0]
    ny = column + step[1]

    if 1 <= nx < 9 and 1 <= ny < 9:
        answer += 1
print(answer)

