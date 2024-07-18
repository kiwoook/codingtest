import heapq
import sys
from collections import defaultdict

INF = int(1e9)


def dijkstra(start_node):
    distance = [INF for _ in range(n + 1)]

    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node, weight in graph[now]:
            if distance[node] > dist + weight:
                distance[node] = dist + weight
                heapq.heappush(q, (dist + weight, node))

    return distance


n = int(sys.stdin.readline().rstrip())
a, b, c = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())

graph = defaultdict(list)

closely_list = []

for _ in range(m):
    d, e, length = map(int, sys.stdin.readline().rstrip().split())
    graph[d].append((e, length))
    graph[e].append((d, length))

closely_list.append(dijkstra(a))
closely_list.append(dijkstra(b))
closely_list.append(dijkstra(c))

answer_distance = [INF for _ in range(n + 1)]

for i in range(0, n + 1):
    answer_distance[i] = min(closely_list[0][i], closely_list[1][i], closely_list[2][i])

max_value = max(answer_distance[1:])

for idx, value in enumerate(answer_distance):
    if value == max_value:
        print(idx)
        break
