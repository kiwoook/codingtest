import sys


def find_parent(x):
    global parent

    if parent[x] != x:
        return find_parent(parent[x])

    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().rstrip().split())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    u, v, weight = map(int, sys.stdin.readline().rstrip().split())
    edges.append((u, v, weight))

edges.sort(key=lambda x: x[2])

weight_list = []
for u, v, weight in edges:
    if find_parent(u) != find_parent(v):
        union(u, v)
        weight_list.append(weight)

print(sum(weight_list[:-1]))
