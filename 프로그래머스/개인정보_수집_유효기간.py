def solution(today, terms, privacies):
    answer = []
    dict_term = dict()
    privacy_list = []
    term_list = []
    today = list(map(int, today.split(".")))
    today = today[0] * 12 * 28 + today[1] * 28 + today[2]

    for term in terms:
        t = term.split(" ")
        dict_term[t[0]] = int(t[1]) * 28

    for privacy in privacies:
        p = privacy.split(" ")
        day = list(map(int, p[0].split(".")))
        privacy_list.append(day[0] * 12 * 28 + day[1] * 28 + day[2])
        term_list.append(p[1])

    for idx, privacy in enumerate(privacy_list):
        if today >= privacy_list[idx] + dict_term[term_list[idx]]:
            answer.append(idx + 1)

    return answer

