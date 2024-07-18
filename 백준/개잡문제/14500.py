import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

max_answer = 0


# DFS로는 ㅗ 모양이 구현이 안된다.
def dfs(y, x, depth, current_sum):
    global max_answer, visited

    if depth == 3:
        max_answer = max(max_answer, current_sum)
        return

    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth + 1, current_sum + board[ny][nx])
            visited[ny][nx] = False


# ㅗ 모양 구현
# 4개 다 둘러봤을 경우에만 탐색
# 근데 자연수라서 문제 없는거 같은데
def checking_h(y, x):
    global max_answer
    hap = board[y][x]
    cnt = 0
    # + 모양
    for z in range(4):
        ny = y + dy[z]
        nx = x + dx[z]
        if 0 <= ny < n and 0 <= nx < m:
            hap += board[ny][nx]
            cnt += 1

    if cnt == 4:
        # 만약 cnt가 4개면 하나 빼서 확인
        for z in range(4):
            ny = y + dy[z]
            nx = x + dx[z]
            if 0 <= ny < n and 0 <= nx < m:
                max_answer = max(max_answer, hap - board[ny][nx])
    if cnt == 3:
        # cnt가 3개면 ㅗ모양 이므로 그대로 하면 됨
        max_answer = max(max_answer, hap)


board = []
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for k in range(m):
        visited[i][k] = True
        dfs(i, k, 0, board[i][k])
        visited[i][k] = False
        checking_h(i, k)

print(max_answer)
