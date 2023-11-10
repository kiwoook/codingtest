import heapq


def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    q = []

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for idx, dist in enumerate(distance):
        if idx == 0:
            continue
        if dist <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
