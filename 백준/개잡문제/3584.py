import sys
from collections import defaultdict

sys.setrecursionlimit(100001)


def dfs(depth, node):
    global depth_list
    depth_list[node] = depth

    for visited_node in graph[node]:
        dfs(depth + 1, visited_node)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    graph = defaultdict(list)
    n = int(sys.stdin.readline().rstrip())
    parent = [i for i in range(n + 1)]
    depth_list = [0 for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        parent[b] = a

    # 자기 자신을 가르치는 노드가 있다면 부모 노드이다.
    parent_node = 0
    for i in range(1, n + 1):
        if i == parent[i]:
            parent_node = i
            break

    dfs(0, parent_node)

    a, b = map(int, sys.stdin.readline().rstrip().split())

    # 깊이 맞추기
    while depth_list[a] != depth_list[b]:
        if depth_list[a] > depth_list[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 같이 올라가기
    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)
