import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tmp = sys.stdin.readline().rstrip().split()
    a = []
    for idx, t in enumerate(tmp):
        a.append((idx, t))
    q = deque(a)
    cnt = 0
    answer = -1
    while answer != m:
        value, imp = q.popleft()
        sw = False
        for v, i in q:
            if imp < i:
                sw = True
                break
        if sw:
            q.append((value, imp))
        else:
            answer = value
            cnt += 1

    print(cnt)
