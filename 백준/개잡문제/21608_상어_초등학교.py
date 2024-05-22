import sys
from collections import deque, defaultdict

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n = int(sys.stdin.readline().rstrip())
board = [[0 for _ in range(n)] for _ in range(n)]
like_dict = defaultdict(list)

q = deque([])
for _ in range(n * n):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    like_dict[cmd[0]] = cmd[1:]
    q.append(cmd[0])

while q:
    person = q.popleft()
    max_like = 0
    max_y, max_x = -1, -1
    tmp = []
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                like = 0
                empty = 0
                for j in range(4):
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if 0 <= ny < n and 0 <= nx < n:
                        if board[ny][nx] in like_dict[person]:
                            like += 1
                        if board[ny][nx] == 0:
                            empty += 1
                tmp.append([like, empty, y, x])
    tmp.sort(key=lambda v: (-v[0], -v[1], v[2], v[3]))
    board[tmp[0][2]][tmp[0][3]] = person

answer = 0

for y in range(n):
    for x in range(n):
        person = board[y][x]
        like = 0
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            if 0 <= ny < n and 0 <= nx < n:
                for like_person in like_dict[person]:
                    if board[ny][nx] == like_person:
                        like += 1
        if like > 0:
            answer += 10 ** (like - 1)

print(answer)
