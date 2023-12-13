from collections import deque


def solution(gems):
    gems_set = set(gems)
    start, end = 0, 0

    first, second = 0, 10000

    q = deque([])

    if len(gems_set) == 1:
        return [1, 1]
    sw = 0

    while len(gems) >= end >= start:
        # set으로 변환하면 시간오래걸린다. 어떻게할깡...
        if set(q) == gems_set and end == len(gems):
            print(start, end)
            sw = 1
            if len(q) == 0:
                break
            q.popleft()
            start += 1
            if end - start < second - first:
                first, second = start, end
        else:
            q.append(gems[end])
            end += 1

    if not sw:
        return [1, len(gems)]

    return [first, second]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "B", "B", "B", "C", "D", "D", "D", "D", "D", "D", "B", "C", "A"]))
