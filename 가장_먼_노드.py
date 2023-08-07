import heapq

graph = []
INF = int(1e9)


def dijkstra(start, n):
    q = []
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


def solution(n, edge):
    global graph
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))

    distance = dijkstra(1, n)

    max_distance = max(distance[1:])

    for i in distance[1:]:
        if i == max_distance:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
