import heapq
import sys

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
path = []
distance = [INF] * (n + 1)
parent = [i for i in range(0, n + 1)]
for _ in range(m):
    first, last, weight = map(int, sys.stdin.readline().strip().split())
    graph[first].append((last, weight))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
path = [str(end)]

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for pos, weight in graph[now]:
        if dist + weight < distance[pos]:
            distance[pos] = dist + weight
            heapq.heappush(q, (dist + weight, pos))
            parent[pos] = now

target = end

while parent[target] != target:
    path.append(str(parent[target]))
    target = parent[target]

path.reverse()

print(distance[end])
print(len(path))
print(' '.join(path))
