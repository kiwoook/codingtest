import heapq
INF = int(1e9)
fare_map = []


def dijkstra(start, n):
    q = []
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in fare_map[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


def solution(n, s, a, b, fares):
    global fare_map
    min_price = 1000000000
    fare_map = [[] for _ in range(n + 1)]

    for fare in fares:
        fare_map[fare[0]].append((fare[1], fare[2]))
        fare_map[fare[1]].append((fare[0], fare[2]))

    distance_to_c = dijkstra(s, n)
    for i in range(n + 1):
        if distance_to_c[i] != INF:
            distance_from_c = dijkstra(i, n)
            if distance_to_c[i] + distance_from_c[a] + distance_from_c[b] < min_price:
                min_price = distance_to_c[i] + distance_from_c[a] + distance_from_c[b]

    return min_price


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
