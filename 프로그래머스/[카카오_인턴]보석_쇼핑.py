from collections import deque, defaultdict


def solution(gems):
    gems_set = set(gems)
    gems_dict = defaultdict(int)
    start, end = 0, 0
    first, second = 0, int(1e9)

    q = deque([])

    if len(gems_set) == 1:
        return [1, 1]
    sw = 0

    while start <= end:
        if len(gems_dict) == len(gems_set):
            sw = 1
            if len(q) == 0:
                break
            q.popleft()
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            if end - start < second - first:
                first, second = start, end
        else:
            if end < len(gems):
                q.append(gems[end])
                gems_dict[gems[end]] += 1
                end += 1
            else:
                start += 1

    if not sw:
        return [1, len(gems)]

    return [first, second]


# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "B", "B", "B", "C", "D", "D", "D", "D", "D", "D", "B", "C", "A"]))
# answer 11 14
