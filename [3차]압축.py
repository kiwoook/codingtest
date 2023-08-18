def solution(msg):
    dictionary = ['0']
    answer = []
    len_msg = len(msg)
    for i in range(ord('A'), ord('Z') + 1):
        dictionary.append(chr(i))
    idx = 0
    while idx < len_msg:
        pointer = 1
        sw = 0
        while msg[idx:idx + pointer] in dictionary:
            pointer += 1
            if idx + pointer > len_msg:
                sw = 1
                break
        if not sw:
            dictionary.append(msg[idx:idx + pointer])
        answer.append(dictionary.index(msg[idx:idx + pointer - 1]))
        idx += pointer-1

    return answer


print(solution("KAKAO"))
