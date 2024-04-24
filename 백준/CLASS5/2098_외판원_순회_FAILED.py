import sys


def dfs(pos, depth, hap):
    global visited, answer, start_idx

    if depth != 0:
        visited[pos] = True

    if 0 < depth < n and pos == start_idx:
        return

    if depth == n and all(visited):
        answer = min(answer, hap)

    for node in range(n):
        if graph[pos][node] != 0 and not visited[node]:
            visited[node] = True
            dfs(node, depth + 1, hap + graph[pos][node])
            visited[node] = False


n = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = int(1e12)
start_idx = -1
for start in range(n):
    visited = [False for _ in range(n)]
    start_idx = start
    dfs(start, 0, 0)

print(answer)
