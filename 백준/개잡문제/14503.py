import sys
from collections import deque

board = []
# 0 북, 1 동, 2 남, 3 서

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque([(r, c)])
cnt = 0

while q:
    y, x = q.popleft()

    # 현재 칸 청소
    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1
    sw = 0
    # 청소되지 않은 빈칸을 확인한다.
    for i in range(1, 5):
        nd = (d + 4 - i) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]

        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
            d = nd
            q.append((ny, nx))
            sw = 1
            break
    # 탐색을 했는데 아무것도 없음
    if sw == 0:
        nd = (d + 2) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 1:
            q.append((ny, nx))
        else:
            break

print(cnt)
