import heapq
import sys

INF = 1e9

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

start = int(input())
distance = [INF] * (v + 1)

# 간선
for _ in range(e):
    first, last, weight = map(int, sys.stdin.readline().split())
    graph[first].append((last, weight))

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

for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(int(dist))
