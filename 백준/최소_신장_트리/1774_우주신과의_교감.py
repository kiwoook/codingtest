import math
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [x for x in range(n + 1)]

coordinate = [None]
edges = []
result = 0

for _ in range(n):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    coordinate.append((y, x))

# 모든 간선들의 거리를 정리한다.
for i in range(1, len(coordinate) - 1):
    for k in range(i + 1, len(coordinate)):
        y1, x1 = coordinate[i]
        y2, x2 = coordinate[k]
        cost = math.sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)
        edges.append((cost, i, k))

edges.sort()

for _ in range(m):
    o1, o2 = map(int, sys.stdin.readline().rstrip().split())
    union_parent(parent, o1, o2)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print("{:.2f}".format(round(result, 2)))
