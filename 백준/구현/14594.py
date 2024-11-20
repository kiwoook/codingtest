import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
answer = 1
wall_list = [0 for _ in range(n + 1)]

break_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

for x, y in break_list:
    for i in range(x, y):
        wall_list[i] = 1

print(wall_list.count(0) - 1)
