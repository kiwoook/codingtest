import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)

board = [i for i in range(101)]
visited = [INF for i in range(101)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x] = y
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    board[u] = v

q = deque([(1, 0)])

answer = INF

while q:
    pos, cnt = q.popleft()
    if pos == 100:
        answer = min(answer, cnt)

    if cnt < visited[pos]:
        visited[pos] = cnt
    else:
        continue

    pos = board[pos]

    for i in range(1, 7):
        if pos + i > 100:
            continue
        q.append((pos + i, cnt + 1))

print(answer)
