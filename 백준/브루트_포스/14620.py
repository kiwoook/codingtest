import sys

answer = int(1e9)

dy = [0, 0, 0, -1, 1]
dx = [0, -1, 1, 0, 0]


def dfs(y, x, flower, total):
    global answer, visited

    if flower == 3:
        answer = min(answer, total)
        return

    for i in range(y, n):
        for j in range(x if i == y else 0, n):
            flag = 0
            hap = 0

            for k in range(5):
                ny = i + dy[k]
                nx = j + dx[k]

                if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx] == 1:
                    flag = 1
                    break
                hap += board[ny][nx]

            if flag == 0:
                for k in range(5):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    visited[ny][nx] = 1

                dfs(i, j, flower + 1, total + hap)

                for k in range(5):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    visited[ny][nx] = 0


n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dfs(0, 0, 0, 0)

print(answer)