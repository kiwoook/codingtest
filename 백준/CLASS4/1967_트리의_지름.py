from collections import defaultdict, deque


def bfs(start):
    visited = [False for _ in range(n + 1)]
    distance = [0 for _ in range(n + 1)]
    q = deque([start])
    parent = 0
    while q:
        node = q.popleft()
        visited[node] = True

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                distance[neighbor] += weight
                print(neighbor)
                q.append(neighbor)


    print(distance)
    return max(distance)


n = int(input())

graph = defaultdict(list)
max_distance = 0

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

bfs(9)

# for i in range(1, n + 1):
#     max_distance = max(max_distance, bfs(i))
#
# print(max_distance)
