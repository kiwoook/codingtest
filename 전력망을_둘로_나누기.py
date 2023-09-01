from collections import deque

graph = []


def count(p, n):
    cnt = 1
    queue = deque([p])
    path = [0 for _ in range(n + 1)]
    path[p] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if path[i] == 0:
                queue.append(i)
                path[i] = 1
                cnt += 1

    return cnt


def solution(n, wires):
    global graph
    min_count = 1e9
    graph = [[] for _ in range(n + 1)]

    # 그래프 생성
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        # 그래프 끊기
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        cnt1 = count(wire[0], n)
        cnt2 = count(wire[1], n)
        if min_count > abs(cnt1 - cnt2):
            min_count = abs(cnt1 - cnt2)
        # 그래프 복구
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    return min_count


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
