import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def find_fish(y, x):
    global board, cnt, shark_size
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance_board = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(y, x)])
    visited[y][x] = True
    board[y][x] = 0
    fish_list = []
    min_distance = int(1e9)
    while q:
        y, x = q.popleft()

        for m in range(4):
            ny = y + dy[m]
            nx = x + dx[m]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                # 그 위치가 작다면 먹고 탈출
                if shark_size > board[ny][nx] > 0:
                    visited[ny][nx] = True
                    distance_board[ny][nx] = distance_board[y][x] + 1
                    q.append((ny, nx))
                    if min_distance > distance_board[ny][nx]:
                        fish_list = [(ny, nx, distance_board[ny][nx])]
                        min_distance = distance_board[ny][nx]

                    if min_distance == distance_board[ny][nx]:
                        fish_list.append((ny, nx, distance_board[ny][nx]))
                        min_distance = distance_board[ny][nx]

                elif shark_size == board[ny][nx] or board[ny][nx] == 0:
                    visited[ny][nx] = True
                    distance_board[ny][nx] = distance_board[y][x] + 1
                    q.append((ny, nx))

    # 모두 뒤졌는데 못찾았음

    if len(fish_list) == 0:
        return -1, -1, -1
    else:
        fish_list.sort(key=lambda x: (x[0], x[1], x[2]))
        y, x, d = fish_list[0]
        cnt += 1
        if shark_size == cnt:
            cnt = 0
            shark_size += 1
        return y, x, d


n = int(sys.stdin.readline().rstrip())

board = []

shark_size = 2
cnt = 0

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

shark_y = -1
shark_x = -1
for i in range(n):
    for k in range(n):
        if board[i][k] == 9:
            shark_x = k
            shark_y = i

time = 0
while 1:
    shark_y, shark_x, distance = find_fish(shark_y, shark_x)
    if distance == -1:
        break
    time += distance

print(time)
