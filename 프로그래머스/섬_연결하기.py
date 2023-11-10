from collections import defaultdict
import heapq


def solution(n, costs):
    answer = 0
    adjacent_edges = defaultdict(list)
    for node1, node2, weight in costs:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    connected = {0}
    candidate_edge = adjacent_edges[0]
    heapq.heapify(candidate_edge)

    while candidate_edge:
        weight, node1, node2 = heapq.heappop(candidate_edge)
        # 사이클 있는지 확인 후 연결
        if node2 not in list(connected):
            connected.add(node2)
            answer += weight

            for edge in adjacent_edges[node2]:
                if edge[2] not in connected:
                    heapq.heappush(candidate_edge, edge)
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
