import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = 0


def dfs(y, x, move, visited):
    global answer
    answer = max(answer, move)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and visited[ord(board[ny][nx])] == 0:
            visited[ord(board[ny][nx])] = 1
            dfs(ny, nx, move + 1, visited)
            visited[ord(board[ny][nx])] = 0


board = []

r, c = map(int, sys.stdin.readline().rstrip().split())

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

vs = [0 for _ in range(100)]
vs[ord(board[0][0])] = 1
dfs(0, 0, 1, vs)
print(answer)