def solution(babbling):
    answer = 0

    using = ["aya", "ye", "woo", "ma"]

    # 연속되는 발음은 안됨
    # 조합해서 만들어야함
    for B in babbling:
        sw = 0
        for i in range(4):
            B = B.replace(using[i], str(i))
        print(B)
        for k in range(len(B) - 1):
            if B[k] == B[k + 1]:
                sw = 1
                break
            elif not '0' <= B[k] <= '3':
                sw = 1
                break
            elif not '0' <= B[k + 1] <= '3':
                sw = 1
                break
        if not '0' <= B[0] <= '3':
            sw = 1
        if not sw:
            answer += 1

    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

