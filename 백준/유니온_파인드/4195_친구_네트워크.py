import sys


def find_parent(x):
    global parent

    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):
    global parent, size

    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a != root_b:
        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a]
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b]


T = int(input())

for _ in range(T):
    F = int(input())
    parent = {}
    size = {}

    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1

        union(a, b)

        cnt = size[find_parent(a)]  # 루트 노드의 집합 크기를 가져옴
        print(cnt)