import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    current, target = map(int, sys.stdin.readline().rstrip().split())
    q = deque([(current, 0, 0)])
    while q:
        pos, move, cnt = q.popleft()
        if pos > target:
            continue
        if pos == target:
            print(cnt)
            break

        for v in range(-1, 2, 1):
            moving = move + v
            if moving <= 0:
                continue
            if 0 <= pos + moving < 2 ** 31:
                q.append((pos + moving, moving, cnt + 1))
