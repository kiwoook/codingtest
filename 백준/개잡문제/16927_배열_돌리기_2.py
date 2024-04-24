import sys
from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def rotate():
    global board
    visited = [[0 for _ in range(m)] for _ in range(n)]
    v = min(n, m) // 2
    # 바깥쪽을 한 다음에 다 돌리면 안쪽 건드는걸로 해야함.
    # 값을 저장하면서 들어가야함

    for i in range(v):
        q = deque([(i, i)])
        tmp_q = deque([])
        direction = 0
        while q:
            y, x = q.popleft()
            tmp_q.append(board[y][x])

            ny = y + dy[direction]
            nx = x + dx[direction]

            # 만약 넘어버렸다면 i를 수정하고 append한다.
            if 0 > ny or ny >= n or 0 > nx or nx >= m or visited[ny][nx] == 1:
                direction = (direction + 1) % 4
                ny = y + dy[direction]
                nx = x + dx[direction]

            if ny == i and nx == i:
                break

            q.append((ny, nx))
        # 큐 값을 회전시키고
        for _ in range(r % (2 * (n - 2 * i) + 2 * (m - 2 * i) - 4)):
            tmp_q.appendleft(tmp_q.pop())

        # 다시 넣는 작업
        q = deque([(i, i)])
        direction = 0
        while q and tmp_q:
            y, x = q.popleft()
            board[y][x] = tmp_q.popleft()
            visited[y][x] = 1

            ny = y + dy[direction]
            nx = x + dx[direction]

            # 만약 넘어버리거나 visited를 만나면 수정한다.
            if 0 > ny or ny >= n or 0 > nx or nx >= m or visited[ny][nx] == 1:
                direction = (direction + 1) % 4
                ny = y + dy[direction]
                nx = x + dx[direction]

            if ny == i and nx == i:
                break

            q.append((ny, nx))


# 1. 기존 바깥쪽 배열을 가져옴
# 2. 한 칸 아래에서부터 재시작

board = []

n, m, r = map(int, sys.stdin.readline().rstrip().split())
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

rotate()

for j in range(n):
    print(*board[j])
