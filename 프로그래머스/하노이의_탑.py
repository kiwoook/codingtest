answer = []


def hanoi(n, start, target, to):
    global answer
    if n == 1:
        print(start, '->', target)
        answer.append([start, target])
        return
    hanoi(n-1, start, to, target)
    answer.append([start, target])
    hanoi(n-1, to, target, start)


def solution(n):
    global answer

    hanoi(2, 1, 3, 2)

    return answer

# 규칙성이 있으면 재귀를 활용하자.
