import sys

INF = int(1e12)

TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    n, m, w = map(int, sys.stdin.readline().rstrip().split())

    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        graph[s][e] = min(graph[s][e], t)
        graph[e][s] = min(graph[e][s], t)
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        graph[s][e] = min(graph[s][e], -t)

    sw = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
                if j == k and graph[j][k] < 0:
                    print("YES")
                    sw = 1
                    break
            if sw == 1:
                break
        if sw == 1:
            break

    if sw == 0:
        print("NO")
