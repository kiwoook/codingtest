import heapq
import sys


def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = list(range(v + 1))

edges = []
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (cost, a, b))  # 힙에 간선 추가

result = 0

while edges:
    cost, a, b = heapq.heappop(edges)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
