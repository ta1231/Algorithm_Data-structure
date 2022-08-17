n = int(input())
coins = list(map(int, input().split()))
answer = 1
coins.sort()

for coin in coins:
    # answer - 1 까지의 모든 금액을 만들 수 있는 상태라 볼 수 있음

    # answer 금액을 만들 수 없다면
    if answer < coin:
        # 답은 answer이다.
        print(answer)
        break
    # target값을 만들 수 있다면
    else:
        # coin을 더해준다.
        answer += coin




