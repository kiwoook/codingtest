import sys

board = []
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

boomerang = [
    [(0, -1), (1, 0)],
    [(0, -1), (-1, 0)],
    [(-1, 0), (0, 1)],
    [(0, 1), (1, 0)]
]

answer = 0
visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(y, x, hap):
    global answer, visited

    if y == n:
        answer = max(answer, hap)
        return

    next_y, next_x = (y + 1, 0) if x == m - 1 else (y, x + 1)

    if visited[y][x]:
        dfs(next_y, next_x, hap)
        return

    # 부메랑을 배치하는 경우
    for f in range(4):
        dy1, dx1 = y + boomerang[f][0][0], x + boomerang[f][0][1]
        dy2, dx2 = y + boomerang[f][1][0], x + boomerang[f][1][1]

        if 0 <= dy1 < n and 0 <= dy2 < n and 0 <= dx1 < m and 0 <= dx2 < m:
            if not visited[dy1][dx1] and not visited[dy2][dx2]:
                visited[y][x] = visited[dy1][dx1] = visited[dy2][dx2] = 1
                dfs(next_y, next_x, hap + 2 * board[y][x] + board[dy1][dx1] + board[dy2][dx2])
                visited[y][x] = visited[dy1][dx1] = visited[dy2][dx2] = 0

    # 부메랑을 배치하지 않는 경우
    dfs(next_y, next_x, hap)


dfs(0, 0, 0)

print(answer)
