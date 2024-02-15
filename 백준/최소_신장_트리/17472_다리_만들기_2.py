import sys
from collections import deque, defaultdict

INF = int(1e9)


def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    global parent
    a = parent[a]
    b = parent[b]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def island(y, x, sign):
    global board, sign_dict
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(y, x)])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        board[y][x] = sign
        sign_dict[sign].append((y, x))
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and board[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = 1


def move(y, x, sign, p):
    if p == 0:
        for my in range(y - 1, -1, -1):
            if board[my][x] == sign:
                return None, None
            if board[my][x] != 0 and board[my][x] != sign:
                return board[my][x], abs(y - my)
    if p == 1:
        for my in range(y + 1, n):
            if board[my][x] == sign:
                return None, None
            if board[my][x] != 0 and board[my][x] != sign:
                return board[my][x], abs(y - my)
    if p == 2:
        for mx in range(x + 1, m):
            if board[y][mx] == sign:
                return None, None
            if board[y][mx] != 0 and board[y][mx] != sign:
                return board[y][mx], abs(x - mx)
    if p == 3:
        for mx in range(x - 1, -1, -1):
            if board[y][mx] == sign:
                return None, None
            if board[y][mx] != 0 and board[y][mx] != sign:
                return board[y][mx], abs(x - mx)
    return None, None


def shortest_range(sign):
    global range_list
    # 섬의 개수는 6개가 최대 2차원 배열로 정리하여 엣지로 반환
    # 해당 좌표에 대해서 상하좌우를 시전한다. 이때 sign값이랑 같거나 끝자락에 도착하면 종료한다.
    for y, x in sign_dict[sign]:
        for j in range(4):
            destination, distance = move(y, x, sign, j)
            if destination is not None and distance - 1 != 1:
                range_list[sign][destination] = min(range_list[sign][destination], distance - 1)


board = []
n, m = map(int, input().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

cnt = 2
sign_dict = defaultdict(list)
for i in range(n):
    for k in range(m):
        if board[i][k] == 1:
            island(i, k, cnt)
            cnt += 1

range_list = [[INF for _ in range(cnt)] for _ in range(cnt)]

for i in range(2, cnt):
    shortest_range(i)

# 간선 만들기
edges = []

for i in range(2, cnt):
    for k in range(2, cnt):
        if i == k:
            continue
        if range_list[i][k] != INF and range_list[i][k] != 1:
            edges.append((range_list[i][k], i, k))

edges.sort()

parent = [x for x in range(cnt)]
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

sw = 0

# 모든 간선 연결 후 parent 값이 2가 아니라면 -1을 출력한다.
for i in range(2, cnt):
    if find_parent(i) != 2:
        sw = 1
        break
if sw:
    print("-1")
else:
    print(result)
