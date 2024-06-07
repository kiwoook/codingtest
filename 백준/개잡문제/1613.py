import sys
# 위상정렬로 푸는 문제가 아니다...


INF = int(1e9)

n, k = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 0

for middle in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][middle] + graph[middle][end] < graph[start][end]:
                graph[start][end] = 0

s = int(sys.stdin.readline().rstrip())

for _ in range(s):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if graph[a][b] == graph[b][a] == INF:
        print(0)
    elif graph[a][b] < graph[b][a]:
        print(-1)
    else:
        print(1)
