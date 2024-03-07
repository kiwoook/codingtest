import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())


def topology_sort():
    result = []
    q = deque()

    for k in range(1, n + 1):
        if indgree[k] == 0:
            q.append(k)

    while q:
        now = q.popleft()
        result.append(now)
        for k in range(1, n + 1):
            if graph[now][k] == 1:
                indgree[k] -= 1
                if indgree[k] == 0:
                    q.append(k)

    return result


for _ in range(T):
    indgree = dict()
    n = int(sys.stdin.readline().rstrip())
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    for x in range(1, n + 1):
        indgree[x] = 0

    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            graph[lst[i]][lst[j]] = 1
            indgree[lst[j]] += 1

    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indgree[a] += 1
            indgree[b] -= 1
        else:
            graph[b][a] = 0
            graph[a][b] = 1
            indgree[b] += 1
            indgree[a] -= 1

    result = topology_sort()
    if len(result) != n:
        print("IMPOSSIBLE")
    else:
        print(*result)
