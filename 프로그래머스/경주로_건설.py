from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

INF = int(1e9)


def solution(board):
    n, m = len(board), len(board[0])

    # y, x, 방향
    visited = [[[(INF, INF) for _ in range(m)] for _ in range(n)] for _ in range(4)]

    for i in range(4):
        visited[i][0][0] = (0, 0)

    q = deque([])
    for i in range(4):
        ny, nx = dy[i], dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
            visited[i][ny][nx] = (1, 0)
            q.append((ny, nx, 1, 0, i))

    while q:
        y, x, straight, corner, turn = q.popleft()
        if board[y][x] == 1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                new_straight = straight + 1
                new_corner = corner + (1 if turn != i else 0)
                if new_straight + new_corner * 5 < visited[i][ny][nx][0] + visited[i][ny][nx][1] * 5:
                    visited[i][ny][nx] = (new_straight, new_corner)
                    q.append((ny, nx, new_straight, new_corner, i))

    # 모든 방향 중 가장 작은 값을 선택
    answer = INF
    for i in range(4):
        answer = min(answer, visited[i][n - 1][m - 1][0] * 100 + visited[i][n - 1][m - 1][1] * 500)

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))
