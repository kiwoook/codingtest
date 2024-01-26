import sys

sys.setrecursionlimit(1001)


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


n = int(input())
m = int(sys.stdin.readline().rstrip())

parent = [x for x in range(n + 1)]
for i in range(n):
    union_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for idx, node in enumerate(union_list):
        if idx == i:
            continue
        if node == 1:
            if find_parent(i + 1) != find_parent(idx + 1):
                union_parent(i + 1, idx + 1)
path = list(map(int, sys.stdin.readline().rstrip().split()))
sw = 0
if len(path) == 1:
    print("YES")
else:
    for p in path[1:]:
        if parent[p] != parent[path[0]]:
            sw = 1
            break
    if sw == 0:
        print("YES")
    else:
        print("NO")
