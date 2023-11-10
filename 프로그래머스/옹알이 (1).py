def solution(babbling):
    answer = 0

    using = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        if len(babble) > 10:
            continue
        tmp_using = using[:]
        visited = [0 for _ in range(4)]
        i = 0
        while i < 4:
            if visited[i] == 0 and tmp_using[i] in babble:
                babble = babble.replace(tmp_using[i], " ")
                visited[i] = 1
                i = -1
            i += 1

        babble = babble.strip()
        if len(babble) == 0:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
