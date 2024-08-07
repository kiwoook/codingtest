import sys

n = int(sys.stdin.readline().rstrip())

drink_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
answer = drink_list.pop()

for i in range(len(drink_list)):
    answer += drink_list[i] / 2

print(f"{round(answer, 5)}")
