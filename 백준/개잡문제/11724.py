import sys


def is_parent(x):
    global parent
    while parent[x] != x:
        x = parent[x]
    return x


def union_parent(a, b):
    a = is_parent(a)
    b = is_parent(b)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(0, n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    union_parent(u, v)


print(parent)
print(len(set(parent[1:])))
