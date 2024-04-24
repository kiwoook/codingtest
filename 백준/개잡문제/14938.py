import heapq
import sys
from collections import defaultdict

INF = int(1e9)

def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


n, m, r = map(int, sys.stdin.readline().rstrip().split())
item_list = [0]
item_list.extend(list(map(int, sys.stdin.readline().rstrip().split())))

graph = defaultdict(list)

for _ in range(r):
    a, b, L = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, L))
    graph[b].append((a, L))

answer = 0

for pos in range(1, n + 1):
    v = 0
    distance = [INF for _ in range(n + 1)]
    dijkstra(pos)
    for i in range(1, n + 1):
        if distance[i] <= m:
            v += item_list[i]
    answer = max(answer, v)

print(answer)