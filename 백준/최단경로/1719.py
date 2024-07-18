import heapq
import sys
from collections import defaultdict

INF = int(1e9)


def dijkstra(start):
    global previous_nodes
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    previous_nodes = [i for i in range(n + 1)]

    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for neighbor, weight in graph[now]:
            if dist + weight < distance[neighbor]:
                distance[neighbor] = dist + weight
                previous_nodes[neighbor] = now
                heapq.heappush(q, (dist + weight, neighbor))

    return previous_nodes


def get_last(end):
    path = [end]
    current_node = end

    while current_node != previous_nodes[current_node]:
        path.append(current_node)
        current_node = previous_nodes[current_node]  # 경로를 반전시켜 올바른 순서로 반환

    return path[-1]


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for node in range(1, n + 1):
    answer = []
    previous_nodes = dijkstra(node)
    for end_node in range(1, n + 1):
        if node == end_node:
            answer.append("-")
            continue
        answer.append(get_last(end_node))
    print(*answer)
