import sys
from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, sys.stdin.readline().rstrip().split())

fireball_q = deque([])
for _ in range(m):
    # r,c 위치 v 지량 s 속력, d 방향
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    cmd[0] = cmd[0] - 1
    cmd[1] = cmd[1] - 1
    fireball_q.append(cmd)

for _ in range(k):
    # 무게 저장하는 보드
    weight_board = [[0 for _ in range(n)] for _ in range(n)]
    # 움직인 파이어볼의 개수를 저장하는 보드
    cnt_board = [[0 for _ in range(n)] for _ in range(n)]
    # 방향에 대해 저장하는 보드
    direction_board = [[[] for _ in range(n)] for _ in range(n)]
    # 속력 저장 보드
    speed_board = [[0 for _ in range(n)] for _ in range(n)]

    while fireball_q:
        r, c, v, s, d = fireball_q.popleft()
        # 파이어볼의 위치를 변경한다.
        r = (r + dy[d] * s) % n
        c = (c + dx[d] * s) % n

        weight_board[r][c] += v
        cnt_board[r][c] += 1
        speed_board[r][c] += s
        direction_board[r][c].append(d)

    tmp_list = []

    # 2개 이상 파이어볼이 들어간 것을 체크한다.
    for y in range(n):
        for x in range(n):
            if cnt_board[y][x] >= 2:
                v = weight_board[y][x] // 5
                s = speed_board[y][x] // cnt_board[y][x]
                if v == 0:
                    continue
                # 디렉션 홀수, 짝수 탐지
                sw = 0
                for direction in direction_board[y][x]:
                    if direction % 2 != 1:
                        sw += 1
                    else:
                        sw -= 1
                if sw == cnt_board[y][x] or sw == -cnt_board[y][x]:
                    for direction in range(0, 8, 2):
                        tmp_list.append((y, x, v, s, direction))
                else:
                    for direction in range(1, 8, 2):
                        tmp_list.append((y, x, v, s, direction))
            if cnt_board[y][x] == 1:
                tmp_list.append((y, x, weight_board[y][x], speed_board[y][x], direction_board[y][x][0]))

    fireball_q = deque(tmp_list)

answer = 0
while fireball_q:
    r, c, v, s, d = fireball_q.popleft()
    answer += v

print(answer)
