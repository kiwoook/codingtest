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


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    parent = [x for x in range(n + 1)]
    edges = []

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        edges.append((a, b))

    result = 0
    for edge in edges:
        a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1

    print(result)
