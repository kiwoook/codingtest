import sys
from collections import defaultdict, deque


def tripology_sort():
    global dp

    q = deque([])
    # 진입 차수가 0인 것을 탐색해야한다.
    for i in range(1, n + 1):
        if indgree[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        pos = q.popleft()
        for node in graph[pos]:
            indgree[node] -= 1
            dp[node] = max(dp[node], dp[pos] + cost[node])
            if indgree[node] == 0:
                q.append(node)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    cost = [0]
    n, k = map(int, sys.stdin.readline().rstrip().split())
    cost.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    graph = defaultdict(list)
    indgree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    for _ in range(k):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        graph[s].append(e)
        indgree[e] += 1

    tripology_sort()
    w = int(sys.stdin.readline().rstrip())
    print(dp[w])
