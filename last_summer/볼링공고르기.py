# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
#
# count = 0
#
# for i in range(n - 1):
#     for j in range(i, n):
#         if balls[i] != balls[j]:
#             count += 1
#         else:
#             continue
# print(count)

'''
문제를 효과적으로 풀기 위해 무게마다 볼링공이 몇 개 있는지를 계산해야한다.
A가 1인 공을 선택할 때의 경우의 수는
1(무게가 1인 공의 개수) * 4(B가 선택하는 경우의 수) = 4가지의 경우가 있다.
A가 2인 공을 선택할 때의 경우의 수는
2(무게가 2인 공의 개수) * 2(B가 선택하는 경우의 수) = 4가지의 경우가 있다.
A가 3인 공을 선택할 때의 경우의 수는
2(무게가 3인 공의 개수) * 0(B가 선택하는 경우의 수) = 0가지의 경우가 있다.
'''
import collections

n, m = map(int, input().split())
data = list(map(int, input().split()))

counter = collections.Counter(data)

answer = 0
for i in range(1, m + 1):
    # 선택한 볼링공을 제외한 볼링공의 개수 update
    n -= counter[i]
    # 선택한 볼링공의 개수 * 선택가능한 볼링공의 개수
    answer += counter[i] * n
print(answer)