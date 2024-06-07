import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rstrip().split())

board = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

# 불과 사람 위치 찾기
person_q = deque([])
fire_q = deque([])

visited = [[0] * c for _ in range(r)]
cnt_board = [[0] * c for _ in range(r)]
fire_visited = [[0] * c for _ in range(r)]

for i in range(r):
    for k in range(c):
        if board[i][k] == 'J':
            person_q.append((i, k))
            visited[i][k] = 1
        if board[i][k] == 'F':
            fire_q.append((i, k))
            fire_visited[i][k] = 1

while person_q:
    # 먼저 불의 위치를 지정시킨다.
    tmp_q = deque([])
    while fire_q:
        fire_y, fire_x = fire_q.popleft()

        for i in range(4):
            ny = fire_y + dy[i]
            nx = fire_x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and fire_visited[ny][nx] == 0 and board[ny][nx] != '#':
                fire_visited[ny][nx] = 1
                tmp_q.append((ny, nx))

    fire_q = tmp_q

    # 사람의 위치를 지정한다.
    tmp_person_q = deque([])
    while person_q:
        p_y, p_x = person_q.popleft()
        for i in range(4):
            ny = p_y + dy[i]
            nx = p_x + dx[i]
            if not (0 <= ny < r and 0 <= nx < c):
                print(cnt_board[p_y][p_x] + 1)
                sys.exit(0)  # 정상적으로 탈출하면 프로그램 종료

            if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == 0 and fire_visited[ny][nx] == 0 and board[ny][
                nx] != '#':
                visited[ny][nx] = 1
                tmp_person_q.append((ny, nx))
                cnt_board[ny][nx] = cnt_board[p_y][p_x] + 1

    person_q = tmp_person_q

print("IMPOSSIBLE")
