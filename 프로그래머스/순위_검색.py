from collections import defaultdict


def binary_search(keys, target):
    left, right = 0, len(keys) - 1
    while left <= right:
        mid = (left + right) // 2
        if keys[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def solution(info, query):
    answer = []
    lang_dict = defaultdict(set)
    occupation_dict = defaultdict(set)
    career_dict = defaultdict(set)
    food_dict = defaultdict(set)
    score_dict = dict()

    for idx, value in enumerate(info):
        arr = value.split(" ")
        lang_dict[arr[0]].add(idx)
        occupation_dict[arr[1]].add(idx)
        career_dict[arr[2]].add(idx)
        food_dict[arr[3]].add(idx)
        score_dict[idx] = int(arr[4])

    score_list = sorted(score_dict.items(), key=lambda x: x[1])

    for value in query:
        # 마지막 query 재나열
        arr = value.split(" and ")
        tmp = arr.pop().split(" ")
        for t in tmp:
            arr.append(t)

        set_list = [set() for _ in range(5)]
        tmp_set = set()
        for idx, a in enumerate(arr):

            if a == '-':
                set_list[idx] = set(i for i in range(len(info)))
                continue
            if idx == 0:
                set_list[0] = lang_dict[a]
            if idx == 1:
                set_list[1] = occupation_dict[a]
            if idx == 2:
                set_list[2] = career_dict[a]
            if idx == 3:
                set_list[3] = food_dict[a]
            if idx == 4:
                tmp_set = (set_list[0].intersection(set_list[1], set_list[2], set_list[3]))
                idx = binary_search(score_list, int(a))
                for v in score_list[idx:]:
                    set_list[4].add(v[0])
        result_set = tmp_set.intersection(set_list[4])

        answer.append(len(result_set))
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
