def solution(s):
    answer = [-1] * len(s)
    for i in range(len(s) - 1, -1, -1):
        idx = s[:i].rfind(s[i])
        if idx != -1:
            answer[i] = i - idx

    return answer


print(solution("banana"))
