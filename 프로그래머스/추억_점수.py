def solution(name, yearning, photos):
    answer = []
    score = dict(zip(name,yearning))

    for photo in photos:
        cnt = 0
        for p in photo:
            if p in name:
                cnt += score[p]
        answer.append(cnt)

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
