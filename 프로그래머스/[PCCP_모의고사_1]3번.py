answer = []


def trace_gene(depth, pos):
    if depth == 0:
        return "Rr"

    parent_gene = trace_gene(depth - 1, pos // 4)

    if parent_gene == "RR":
        return "RR"
    elif parent_gene == "rr":
        return "rr"
    else:
        return ["RR", "Rr", "Rr", "rr"][pos % 4]


def solution(queries):
    global answer
    answer = []

    for query in queries:
        depth, pos = query
        depth -= 1
        pos -= 1

        result = trace_gene(depth, pos)
        answer.append(result)

    return answer