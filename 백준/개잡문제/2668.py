import sys


def dfs(start, node):
    global visited, answer_set
    if visited[node] == 1:
        if start == node:
            for idx, value in enumerate(visited):
                if value == 1:
                    answer_set.add(idx)
        return

    visited[node] = 1
    dfs(start, graph[node])
    visited[node] = 0


n = int(sys.stdin.readline().rstrip())
graph = dict()

answer_set = set()
for i in range(1, n + 1):
    graph[i] = int(sys.stdin.readline().rstrip())

visited = [0 for _ in range(n + 1)]

for start_node in range(1, n + 1):
    dfs(start_node, start_node)

answer_list = sorted(list(answer_set))

print(len(answer_list))
for answer in answer_list:
    print(answer)
