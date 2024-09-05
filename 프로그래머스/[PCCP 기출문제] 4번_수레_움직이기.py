dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

INF = int(1e9)
answer = INF


def dfs(n, m, count, red_pos, blue_pos, red_goal, blue_goal, visited_red, visited_blue, flag, maze):
    # 백트래킹으로 시도한다.
    global answer

    if red_pos == red_goal and blue_pos == blue_goal:
        answer = min(answer, count // 2)
        return
    elif red_pos == red_goal:
        # 빨강색은 고정시킨다.
        count += 1
        flag = 1
    elif blue_pos == blue_goal:
        count += 1
        flag = 2

    if flag == 2 or count % 2 == 1:
        y, x = red_pos
        sw = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited_red[ny][nx] and (ny, nx) != blue_pos and maze[ny][nx] != 5:
                # 파랑색이 있는데면 가지 못함
                sw = 1
                visited_red[ny][nx] = True
                dfs(n, m, count + 1, (ny, nx), blue_pos, red_goal, blue_goal, visited_red, visited_blue, flag, maze)
                visited_red[ny][nx] = False
        if sw == 0:
            return

    if flag == 1 or count % 2 == 0:
        y, x = blue_pos
        sw = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited_blue[ny][nx] and (ny, nx) != red_pos and maze[ny][nx] != 5:
                sw = 1
                visited_blue[ny][nx] = True
                dfs(n, m, count + 1, red_pos, (ny, nx), red_goal, blue_goal, visited_red, visited_blue, flag, maze)
                visited_blue[ny][nx] = False


def solution(maze):
    global answer
    n, m = len(maze), len(maze[0])

    red_pos, blue_pos, red_goal, blue_goal = (-1, -1), (-1, -1), (-1, -1), (-1, -1)

    visited_red = [[False] * m for _ in range(n)]
    visited_blue = [[False] * m for _ in range(n)]

    for i in range(n):
        for k in range(m):
            if maze[i][k] == 1:
                visited_red[i][k] = True
                red_pos = (i, k)
            elif maze[i][k] == 2:
                visited_blue[i][k] = True
                blue_pos = (i, k)
            elif maze[i][k] == 3:
                red_goal = (i, k)
            elif maze[i][k] == 4:
                blue_goal = (i, k)

    # 빨강부터 하는 방법 과 파랑부터 하는 방법 나누기
    dfs(n, m, 0, red_pos, blue_pos, red_goal, blue_goal, visited_red, visited_blue, 0, maze)
    dfs(n, m, 0, red_pos, blue_pos, red_goal, blue_goal, visited_red, visited_blue, 0, maze)

    return 0 if answer == INF else answer


# print(solution([[1, 4], [0, 0], [2, 3]]))
print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]))
