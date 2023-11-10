def solution_1(quiz):
    answer = []

    for q in quiz:
        arr = q.split('=')
        if eval(arr[0]) == int(arr[1]):
            answer.append("O")
        else:
            answer.append("X")

    # EVAL은 보안문제를 발생시키니깐 사용하지 말자!
    # 코테 면접에서 왜 썻냐하면 할 말이 없다...

    return answer


def solution(quiz):
    answer = []

    for q in quiz:
        math_expr = q.split(" ")
        if math_expr[1] == '-':
            if int(math_expr[0]) - int(math_expr[2]) == int(math_expr[-1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(math_expr[0]) + int(math_expr[2]) == int(math_expr[-1]):
                answer.append("O")
            else:
                answer.append("X")

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
