import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

max_answer = 0


# DFS로는 ㅗ 모양이 구현이 안된다.
def dfs(y, x, depth, hap):
    global max_answer, visited

    if depth == 3:
        max_answer = max(max_answer, hap)
        return

    for z in range(4):
        ny = y + dy[z]
        nx = x + dx[z]
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, depth + 1, hap + board[ny][nx])
            visited[ny][nx] = 0


# ㅗ 모양 구현
def checking_h(y, x):
    global max_answer
    hap = board[y][x]

    # 십자가 모양
    for z in range(4):
        ny = y + dy[z]
        nx = x + dx[z]
        if 0 <= ny < 4 and 0 <= nx < 4:
            hap += board[ny][nx]

    # 하나씩 빼서 ㅗ 모양 구현
    for z in range(4):
        ny = y + dy[z]
        nx = x + dx[z]
        if 0 <= ny < 4 and 0 <= nx < 4:
            max_answer = max(max_answer, hap - board[ny][nx])
        else:
            max_answer = max(max_answer, hap)


board = []
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for k in range(m):
        visited[i][k] = 1
        dfs(i, k, 0, board[i][k])
        visited[i][k] = 0
        checking_h(i, k)

print(max_answer)
