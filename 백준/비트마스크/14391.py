import sys

answer = 0


def sum_number(y, x, idx):
    global n, m, visited

    dy = [0, 1]
    dx = [1, 0]

    value = board[y][x]
    visited[y][x] = 1

    ny = y + dy[idx]
    nx = x + dx[idx]

    while ny < n and nx < m and bit_mask[ny][nx] == idx and visited[ny][nx] == 0:
        value += board[ny][nx]
        visited[ny][nx] = 1
        ny = ny + dy[idx]
        nx = nx + dx[idx]

    return int(value)


n, m = map(int, sys.stdin.readline().rstrip().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

for v in range(0, 2 ** (n * m)):
    v = bin(v)[2:].zfill(n * m)
    bit_mask = [list(map(int, v[i:i + m])) for i in range(0, n * m, m)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    total = 0
    for i in range(n):
        for k in range(m):
            if visited[i][k] == 0:
                total += sum_number(i, k, bit_mask[i][k])

    answer = max(answer, total)

print(answer)
