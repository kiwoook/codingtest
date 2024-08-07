import sys

n = int(sys.stdin.readline().rstrip())

milk_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

answer = 0
for idx, milk in enumerate(milk_list):
    if idx > 0 and (idx + 1) % 3 == 0:
        continue
    answer += milk

print(answer)
