from collections import deque


def solution(gems):
    gems_set = set(gems)
    start, end = 0, 0
    first, second = 0, 100000
    q = deque([])

    if len(gems_set) == 1:
        return [1, 1]
    sw = 0
    while end < len(gems):
        if set(q) == gems_set:
            sw = 1
            q.popleft()
            start += 1
            if end - start < second - first:
                first, second = start, end
        else:
            end += 1
            q.append(gems[end - 1])
    if not sw:
        return [1, len(gems)]

    return [first, second]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
