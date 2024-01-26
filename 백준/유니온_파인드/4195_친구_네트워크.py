import sys


def find_parent(x):
    global parent

    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):
    global parent

    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a != root_b:
        parent[root_b] = root_a


T = int(input())

for _ in range(T):
    F = int(input())
    parent = {}
    root = ''
    friend = set()
    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()

        if len(root) == 0:
            root = a
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b

        if find_parent(a) != find_parent(b):
            union(a, b)

        cnt = 0

        for key in parent.keys():
            if parent[key] != root:
                find_parent(key)
            if parent[key] == root:
                cnt += 1

        print(cnt)
