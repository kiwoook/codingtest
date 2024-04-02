from collections import defaultdict, deque

n = int(input())

arr = list(map(int, input().split()))

graph = defaultdict(list)
root_node = -1
for idx, value in enumerate(arr):
    if value == -1:
        root_node = idx
        continue
    graph[value].append(idx)

remove_value = int(input())

# 제거 작업
for key, values in graph.items():
    if key == remove_value:
        graph[key] = None

    for value in values:
        if value == remove_value:
            graph[key].remove(value)

# BFS로 탐색 작업
q = deque([root_node])
answer = 0

while q:

    pos = q.popleft()
    if remove_value == pos:
        continue

    if graph.get(pos) is None or len(graph[pos]) == 0:
        answer += 1
        continue

    for node in graph[pos]:
        q.append(node)

print(answer)
