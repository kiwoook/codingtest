
def solution(record):
    answer = []
    nickname = dict()
    for r in record:
        command = list(r.split(" "))
        if command[0] == "Enter":
            nickname[command[1]] = command[2]
        if command[0] == "Change":
            nickname[command[1]] = command[2]

    for r in record:
        command = list(r.split(" "))
        if command[0] == "Enter":
            answer.append(nickname[command[1]]+"님이 들어왔습니다.")
        if command[0] == "Leave":
            answer.append(nickname[command[1]]+"님이 나갔습니다.")
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
print(solution( ["Enter uid1234 Muzi", "Change uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo"]))