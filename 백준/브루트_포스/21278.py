import sys
from collections import defaultdict, deque
from itertools import combinations


def bfs(chicken_pos_tuple):
    pos1, pos2 = chicken_pos_tuple

    distance_list = [0 for _ in range(n + 1)]
    chicken_list = [0 for _ in range(n + 1)]
    chicken_list[pos1], chicken_list[pos2] = 1, 1

    for start_node in range(1, n + 1):
        visited = [False for _ in range(n + 1)]
        q = deque([(start_node, 0)])

        while q:
            node, cnt = q.popleft()
            if chicken_list[node] == 1:
                distance_list[start_node] = cnt
                break

            for ad_node in graph[node]:
                if not visited[ad_node]:
                    visited[ad_node] = True
                    q.append((ad_node, cnt + 1))

    return sum(distance_list)


graph = defaultdict(list)
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 어차피 최단 위치로 돌아갈 건데 왕복으로 할 필요는 없을 듯?

node_list = [i for i in range(1, n + 1)]

comb_list = list(combinations(node_list, 2))

min_distance = int(1e9)
answer = []

for comb in comb_list:
    v = bfs(comb)
    if min_distance > v:
        answer = [comb[0], comb[1], v * 2]
        min_distance = v

print(*answer)
