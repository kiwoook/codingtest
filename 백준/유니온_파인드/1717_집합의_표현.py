import sys

sys.setrecursionlimit(100000)

def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [x for x in range(n + 1)]

for _ in range(m):
    z, one, two = map(int, sys.stdin.readline().rstrip().split())
    if z == 0:
        if find_parent(one) != find_parent(two):
            union(one, two)
    else:
        if find_parent(one) != find_parent(two):
            print("NO")
        else:
            print("YES")
