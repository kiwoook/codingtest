
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
indgree = dict()

for x in range(1, n + 1):
    indgree[x] = 0

for _ in range(m):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    for z in range(1, lst[0]):
        graph[lst[z]].append(lst[z + 1])
        indgree[lst[z + 1]] += 1

answer = topology_sort()

if len(answer) != n:
    print("0")
else:
    for a in answer:
        print(a)
