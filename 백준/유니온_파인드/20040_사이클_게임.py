import sys

sys.setrecursionlimit(500001)


def find_parent(x):
    global parent

    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(a, b):
    global parent

    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [x for x in range(n)]

sw = 0
for i in range(m):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())

    if find_parent(node1) == find_parent(node2):
        print(i + 1)
        sw = 1
        break
    else:
        union_parent(node1, node2)

if not sw:
    print("0")
