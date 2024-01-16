import heapq
import sys
from collections import defaultdict

INF = int(1e9)


def dijkstra(graph, start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for pos, weight in graph[now]:
            if dist + weight < distance[pos]:
                distance[pos] = dist + weight
                heapq.heappush(q, (dist + weight, pos))


n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
distance = [INF for _ in range(n + 1)]
dijkstra(graph, s)
print(distance[e])
