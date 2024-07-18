import sys
from collections import defaultdict

INF = 1

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)

distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, n + 1):
        if i == k:
            distance[i][k] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    distance[a][b] = 0

for m in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][m] + distance[m][b])

for start in range(1, n + 1):
    for end in range(1, n + 1):
        if distance[start][end] == 0:
            distance[end][start] = 0

for i in range(1, n + 1):
    cnt = 0
    print(sum(distance[i][1:]))
