from collections import Counter


def solution(s):
    answer = []
    tuple_list = []
    len_s = len(s)
    s = s[1:len_s - 1]
    start_idx = 0
    for i in range(len(s)):
        if s[i] == '{':
            start_idx = i
        if s[i] == '}':
            tuple_list.append(list(map(int, s[start_idx + 1:i].split(','))))

    tuple_list = sum(tuple_list, [])

    for x in Counter(tuple_list).most_common():
        answer.append(x[0])

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
