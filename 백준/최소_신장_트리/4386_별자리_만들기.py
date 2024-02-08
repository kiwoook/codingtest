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


n = int(input())
parent = [x for x in range(n)]

points = []
edges = []
result = 0
for i in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    points.append((i, x, y))

for i in range(n - 1):
    for k in range(i + 1, n):
        a, x1, y1 = points[i]
        b, x2, y2 = points[k]
        edges.append((math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2), a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(round(result, 2))
