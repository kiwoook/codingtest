import sys
from collections import deque

board = []

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

cloud_q = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for _ in range(m):
    d, s = map(int, sys.stdin.readline().rstrip().split())
    cloud_board = [[0 for _ in range(n)] for _ in range(n)]
    tmp_list = []

    while cloud_q:
        cloud_y, cloud_x = cloud_q.popleft()
        for _ in range(s):
            cloud_y = (cloud_y + dy[d]) % n
            cloud_x = (cloud_x + dx[d]) % n
        board[cloud_y][cloud_x] += 1
        cloud_board[cloud_y][cloud_x] = 1
        tmp_list.append((cloud_y, cloud_x))

    for t_y, t_x in tmp_list:
        cnt = 0
        for i in range(2, 9, 2):
            ny = t_y + dy[i]
            nx = t_x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                cnt += 1
        board[t_y][t_x] += cnt

    for y in range(n):
        for x in range(n):
            if board[y][x] >= 2 and cloud_board[y][x] == 0:
                cloud_q.append((y, x))
                board[y][x] -= 2

print(sum(sum(board, [])))
