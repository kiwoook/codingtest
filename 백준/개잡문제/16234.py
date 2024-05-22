import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def move(pos, hap1):
    value = hap1 // len(visited_pos)

    # 만약 value값이 board들의 값과 똑같다면 인구이동을 하지 않은거다.
    def_sw = 0
    for v_y, v_x in pos:
        if board[v_y][v_x] != value:
            def_sw = 1
        board[v_y][v_x] = value
    return def_sw


n, l, r = map(int, sys.stdin.readline().rstrip().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

flag_board = [[0 for _ in range(n)] for _ in range(n)]
answer = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for k in range(n):
            if visited[i][k] == 0:
                visited_pos = []
                queue = deque([(i, k)])
                hap = 0
                visited[i][k] = 1
                while queue:
                    y, x = queue.popleft()
                    visited_pos.append((y, x))
                    hap += board[y][x]

                    for m in range(4):
                        ny = y + dy[m]
                        nx = x + dx[m]

                        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and l <= abs(board[ny][nx] - board[y][x]) <= r:
                            queue.append((ny, nx))
                            visited[ny][nx] = 1
                cnt += move(visited_pos, hap)

    if cnt == 0:
        break

    answer += 1

print(answer)
