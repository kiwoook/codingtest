import sys
from collections import defaultdict, deque


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indgree[i] -= 1
            if indgree[i] == 0:
                q.append(i)

    return result


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)
indgree = defaultdict(int)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indgree[b] += 1

answer = topology_sort()
print(*answer)
