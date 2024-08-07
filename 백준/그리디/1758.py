import sys

n = int(sys.stdin.readline().rstrip())

money_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

answer = 0

for idx, money in enumerate(money_list):
    answer += money - idx if money - idx > 0 else 0

print(answer)
