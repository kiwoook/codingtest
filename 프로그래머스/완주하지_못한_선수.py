from collections import Counter


def solution(participant, completion):
    answer = dict(Counter(participant) - Counter(completion))

    return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
