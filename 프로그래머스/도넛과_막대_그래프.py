from collections import defaultdict


def solution(edges):
    answer = [0, 0, 0, 0]

    graph = defaultdict(list)
    in_dict = defaultdict(int)

    for start, end in edges:
        graph[start].append(end)
        if len(graph[end]) == 0:
            graph[end] = []
        in_dict[end] += 1

    for key, value in graph.items():
        if in_dict[key] == 0 and len(value) >= 2:
            answer[0] = key
        if len(value) == 2 and in_dict[key] >= 2:
            answer[3] += 1
        if len(value) == 0 and in_dict[key] >= 1:
            answer[2] += 1

    answer[1] = len(graph[answer[0]]) - answer[3] - answer[2]

    return answer


print(solution([[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]]))
