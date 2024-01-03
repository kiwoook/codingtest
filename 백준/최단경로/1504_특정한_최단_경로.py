import heapq
import sys


def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[start][i[0]]:
                distance[start][i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


n, e = map(int, input().split())
INF = int(1e9)
distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    first, last, weight = map(int, sys.stdin.readline().strip().split())
    # 무방향이면 반대쪽도 만들어줘야한다!!!!!
    graph[first].append((last, weight))
    graph[last].append((first, weight))

v1, v2 = map(int, input().split())

dijkstra(1)
dijkstra(v1)
dijkstra(v2)

min_value = min(distance[1][v1] + distance[v1][v2] + distance[v2][n],
                distance[1][v2] + distance[v2][v1] + distance[v1][n])

if min_value >= INF:
    print("-1")
else:
    print(min_value)
