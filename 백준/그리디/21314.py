import sys

n = int(sys.stdin.readline().rstrip())
crane_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
m = int(sys.stdin.readline().rstrip())
box_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

if crane_list[0] < box_list[0]:
    print(-1)
    exit(0)

time = 0

while box_list:
    time += 1
    crane_index = 0
    box_index = 0
    while crane_index < n and box_index < len(box_list):
        if crane_list[crane_index] >= box_list[box_index]:
            box_list.pop(box_index)
            crane_index += 1
        else:
            box_index += 1

print(time)