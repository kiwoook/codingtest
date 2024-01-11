import heapq
import sys

test_case = int(input())
INF = 100000000


def dijkstra(s):
    tmp_distance = [INF for _ in range(n + 1)]
    tmp_distance[s] = 0

    q = []
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)

        if tmp_distance[now] < dist:
            continue
        for pos, weight in graph[now]:
            if dist + weight < tmp_distance[pos]:
                tmp_distance[pos] = dist + weight
                heapq.heappush(q, (dist + weight, pos))

    return tmp_distance


def ghWeight(one, two):
    # g - h가 연결되어있는지 체크
    if len(graph[one]) != 0:
        for pos, weight in graph[one]:
            if pos == two:
                return weight

    return INF


for _ in range(test_case):
    answer = []
    n, m, t = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    start, g, h = map(int, input().split())
    distance = [[] for _ in range(3)]

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    end_list = []

    for _ in range(t):
        end_list.append(int(sys.stdin.readline().strip()))

    distance[0] = dijkstra(start)
    distance[1] = dijkstra(g)
    distance[2] = dijkstra(h)

    gh_weight = ghWeight(g, h)

    for end in end_list:
        if distance[0][end] >= INF or gh_weight == INF:
            continue
        elif distance[0][g] + gh_weight + distance[2][end] == distance[0][end] or distance[0][h] + gh_weight + distance[1][end] == distance[0][end]:
            answer.append(end)

    if len(answer) != 0:
        answer.sort()
        print(*answer, end='')
    print()

