def solution(id_list, report, limit):
    report = set(report)
    answer = []
    dict_user = dict()
    cnt_user = dict()
    suspend_list = []

    for idl in id_list:
        dict_user[idl] = []
        cnt_user[idl] = 0
    for rep in report:
        a, b = list(rep.split(" "))
        dict_user[a].append(b)
        cnt_user[b] += 1

    for key, value in cnt_user.items():
        if value >= limit:
            suspend_list.append(key)

    for user, reported in dict_user.items():
        cnt = sum(1 for suspend in suspend_list if suspend in reported)
        answer.append(cnt)

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
