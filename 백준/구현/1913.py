import sys
from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())

target_y, target_x = -1, -1
board = [[0 for _ in range(n)] for _ in range(n)]

q = deque([(0, 0)])
value = n * n
current = 0

while q:
    y, x = q.popleft()
    board[y][x] = value
    if value == target:
        target_y, target_x = y, x

    value -= 1

    ny = y + dy[current]
    nx = x + dx[current]

    if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] > 0:
        current = (current + 1) % 4
        ny = y + dy[current]
        nx = x + dx[current]
    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
        q.append((ny, nx))

for i in range(n):
    print(*board[i])
print(target_y + 1, target_x + 1)
