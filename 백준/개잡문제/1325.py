import sys
from collections import defaultdict, deque

max_cnt = 0


def bfs(node):
    global max_cnt
    visited = [False for _ in range(n + 1)]
    q = deque([node])
    visited[node] = True
    cnt = 0
    while q:
        node = q.popleft()

        for nd in graph[node]:
            if not visited[nd]:
                visited[nd] = True
                q.append(nd)
                cnt += 1

    max_cnt = max(cnt, max_cnt)

    return cnt


graph = defaultdict(list)

n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

cnt_list = []

for start_node in range(1, n + 1):
    v = bfs(start_node)
    cnt_list.append((start_node, v))

cnt_list.sort(key=lambda x: (-x[1], x[0]))

answer = []
for key, value in cnt_list:
    if value == max_cnt:
        answer.append(key)

print(*answer)
