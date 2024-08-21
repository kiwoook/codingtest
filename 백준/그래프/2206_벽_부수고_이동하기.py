import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

q = deque([(0, 0, 1, 0)])
visited[0][0][0] = True

answer = -1

while q:
    y, x, cnt, flag = q.popleft()

    if y == n - 1 and x == m - 1:
        answer = cnt
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 1 and flag == 0 and not visited[ny][nx][1]:
                visited[ny][nx][1] = True
                q.append((ny, nx, cnt + 1, 1))
            elif board[ny][nx] == 0 and not visited[ny][nx][flag]:
                visited[ny][nx][flag] = True
                q.append((ny, nx, cnt + 1, flag))

print(answer)