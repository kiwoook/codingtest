from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
INF = int(1e9)


def solution(n, m, hole):
    answer = INF

    board = [[0 for _ in range(m)] for _ in range(n)]

    # 구멍 설정 (구멍을 1로 표시)
    for y, x in hole:
        board[y - 1][x - 1] = 1

    # 점프 미사용 BFS
    q = deque([(0, 0)])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0
    while q:
        y, x = q.popleft()

        if y == n - 1 and x == m - 1:  # 목적지 도착
            answer = visited[y][x]
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

    # 점프 사용 BFS
    q = deque([(0, 0, 0)])  # (y, x, 점프 사용 여부)
    visited = [[[INF for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0  # 점프를 사용하지 않은 상태에서 시작

    while q:
        y, x, sw = q.popleft()

        if y == n - 1 and x == m - 1:  # 목적지 도착
            answer = min(answer, visited[y][x][sw])
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                # 벽을 만나고 점프를 아직 안 쓴 경우
                if board[ny][nx] == 1 and sw == 0:
                    nny = ny + dy[i]
                    nnx = nx + dx[i]
                    if 0 <= nny < n and 0 <= nnx < m and board[nny][nnx] == 0 and visited[nny][nnx][1] > visited[y][x][
                        0] + 1:
                        visited[nny][nnx][1] = visited[y][x][0] + 1
                        q.append((nny, nnx, 1))  # 점프 사용 상태로 큐에 추가

                # 벽이 아닌 경우
                elif board[ny][nx] == 0 and visited[ny][nx][sw] > visited[y][x][sw] + 1:
                    visited[ny][nx][sw] = visited[y][x][sw] + 1
                    q.append((ny, nx, sw))

    return answer if answer != INF else -1


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
