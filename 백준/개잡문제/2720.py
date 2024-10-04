import sys

t = int(sys.stdin.readline().rstrip())

money_list = [25, 10, 5, 1]

for _ in range(t):
    answer = []
    money = int(sys.stdin.readline().rstrip())

    for i in range(4):
        answer.append(money // money_list[i])
        money %= money_list[i]

    print(*answer)
