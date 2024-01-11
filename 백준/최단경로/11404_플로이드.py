import sys

INF = int(1e9)

n = int(input())
m = int(input())

distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, n + 1):
        if i == k:
            distance[i][k] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if distance[a][b] != INF:
        distance[a][b] = min(distance[a][b], c)
    else:
        distance[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for i in range(1, n + 1):
    answer = []
    for k in range(1, n + 1):
        if distance[i][k] == INF:
            answer.append("0")
        else:
            answer.append(str(distance[i][k]))
    print(" ".join(answer))
