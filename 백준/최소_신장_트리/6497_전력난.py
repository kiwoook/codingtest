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


m, n = map(int, sys.stdin.readline().rstrip().split())
while m != 0 and n != 0:
    parent = [x for x in range(m + 1)]
    edges = []
    result = 0
    all_cost = 0
    for _ in range(n):
        a, b, cost = map(int, sys.stdin.readline().rstrip().split())
        all_cost += cost
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(all_cost - result)
    m, n = map(int, sys.stdin.readline().rstrip().split())
