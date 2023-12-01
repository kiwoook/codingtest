import sys
from collections import deque

n = int(input())
queue = deque([])

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == '1':
        queue.appendleft(cmd[1])
    if cmd[0] == '2':
        queue.append(cmd[1])
    if cmd[0] == '3':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    if cmd[0] == '4':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop())
    if cmd[0] == '5':
        print(len(queue))
    if cmd[0] == '6':
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    if cmd[0] == '7':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    if cmd[0] == '8':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
