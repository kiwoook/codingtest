import sys


def change_light(idx):
    global lamp_list

    if lamp_list[idx] == 0:
        lamp_list[idx] = 1
    else:
        lamp_list[idx] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
lamp_list = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(m):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))

    if cmd[0] == 1:
        lamp_list[cmd[1] - 1] = cmd[2]
    if cmd[0] == 2:
        for i in range(cmd[1] - 1, cmd[2]):
            change_light(i)
    if cmd[0] == 3:
        for i in range(cmd[1] - 1, cmd[2]):
            lamp_list[i] = 0
    if cmd[0] == 4:
        for i in range(cmd[1] - 1, cmd[2]):
            lamp_list[i] = 1

print(*lamp_list)
