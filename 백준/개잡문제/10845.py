import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque([])

for _ in range(n):
    a = list(sys.stdin.readline().rstrip().split())

    if a[0] == 'push_front':
        q.appendleft(a[1])
    if a[0] == 'push_back':
        q.append(a[1])
    if a[0] == 'pop_front':
        if len(q) >= 1:
            print(q.popleft())
        else:
            print(-1)
    if a[0] == 'pop_back':
        if len(q) >= 1:
            print(q.pop())
        else:
            print(-1)
    if a[0] == 'size':
        print(len(q))
    if a[0] == 'empty':
        if len(q) == 0:
            print("1")
        else:
            print("0")
    if a[0] == 'front':
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])
    if a[0] == 'back':
        if len(q) == 0:
            print("-1")
        else:
            print(q[-1])
