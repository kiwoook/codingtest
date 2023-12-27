from collections import deque


def check(y, x, n, value):
    global a

    visited = [[0 for _ in range(n)] for _ in range(n)]

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    cnt = 1
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        a[y][x] = value

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= ny < n and 0 <= nx < n and a[ny][nx] == '1':
                if visited[ny][nx] == 0:
                    cnt += 1
                    q.append((ny, nx))
                    visited[ny][nx] = 1

    return cnt


n = int(input())

a = []

for i in range(n):
    a.append(list(input()))

num_list = []
apt = 0

for i in range(n):
    for k in range(n):
        if a[i][k] == '1':
            apt += 1
            num_list.append(check(i, k, n, apt))

num_list.sort()

print(apt)
for num in num_list:
    print(num)
