alpha = ['A', 'E', 'I', 'O', "U"]
cnt = 0
answer = 0


def recur(target, branch, depth, word):
    global alpha, cnt, answer

    if target == word:
        answer = cnt
        return

    if depth == 5:
        return

    target += alpha[branch]
    cnt += 1
    print(target)
    for i in range(5):
        recur(target, i, depth + 1, word)


def solution(word):
    global alpha, cnt, answer

    for i in range(5):
        recur("", i, 0, word)

    return answer


print(solution("AAAAE"))
