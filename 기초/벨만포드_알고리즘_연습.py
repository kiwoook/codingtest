import sys


def bellman_ford(start):
    global distance
    distance[start] = 0
    for i in range(n):
        for cur_node, next_node, edge_cost in edges:
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n - 1:
                    return True
    return False


INF = int(1e9)
edges = []

n, m = map(int, input().split())

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for k in range(2, n + 1):
        if distance[k] == INF:
            print("-1")
        else:
            print(distance[k])
