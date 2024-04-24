import sys
from collections import deque

idx = 1

INF = int(1e9)

board = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

hap_list = [[INF for _ in range(n)] for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

q = deque([(0, 0)])
hap_list[0][0] = board[0][0]

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if hap_list[ny][nx] > hap_list[y][x] + board[ny][nx]:
                hap_list[ny][nx] = hap_list[y][x] + board[ny][nx]
                q.append((ny, nx))

print("Problem %d: %d" % (idx, hap_list[n - 1][n - 1]))
idx += 1
while 1:
    board = []
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    hap_list = [[INF for _ in range(n)] for _ in range(n)]

    q = deque([(0, 0)])
    hap_list[0][0] = board[0][0]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if hap_list[ny][nx] > hap_list[y][x] + board[ny][nx]:
                    hap_list[ny][nx] = hap_list[y][x] + board[ny][nx]
                    q.append((ny, nx))
    print("Problem %d: %d" % (idx, hap_list[n - 1][n - 1]))
    idx += 1
