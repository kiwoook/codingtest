def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    for word in s:
        w = word
        for i in range(index):
            w = chr((ord(w) + 1 - ord('a')) % 26 + ord('a'))
            while w in skip:
                w = chr((ord(w) + 1 - ord('a')) % 26 + ord('a'))
        answer += w

    return answer


print(solution("aukks", "wbqd", 5))