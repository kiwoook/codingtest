from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    for idx, b in enumerate(board):
        board[idx] = list(b)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    r_y, r_x = -1, -1
    # R 위치 탐색
    for i in range(n):
        for k in range(m):
            if board[i][k] == 'R':
                r_y, r_x = i, k
                break
        if r_y != -1:
            break

    stack = deque([[r_y, r_x, 0]])

    while stack:
        y, x, cnt = stack.popleft()

        if board[y][x] != 'X':
            print(y,x, cnt)
            board[y][x] = 'X'
            for i in range(4):
                # 끝까지 가는 로직
                ny, nx = y + dy[i], x + dx[i]
                while 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 'D':
                    ny += dy[i]
                    nx += dx[i]
                ny -= dy[i]
                nx -= dx[i]
                stack.append([ny, nx, cnt+1])
                if board[ny][nx] == 'G':
                    return cnt+1

    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	))
