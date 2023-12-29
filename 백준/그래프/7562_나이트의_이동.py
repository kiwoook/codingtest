from collections import deque


def bfs(y, x, target_y, target_x, size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    visited = [[0 for _ in range(size)] for _ in range(size)]

    q = deque([(y, x)])
    visited[y][x] = 1

    dy = [-2, -2, -1, -1, 1, 1, 2, 2]
    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    while q:
        y, x = q.popleft()

        if y == target_y and x == target_x:
            return board[y][x]

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < size and 0 <= nx < size:
                if visited[ny][nx] == 0:
                    q.append((ny, nx))
                    board[ny][nx] = board[y][x] + 1
                    visited[ny][nx] = 1


T = int(input())

for _ in range(T):
    L = int(input())
    y, x = map(int, input().split())
    target_y, target_x = map(int, input().split())

    print(bfs(y, x, target_y, target_x, L))
