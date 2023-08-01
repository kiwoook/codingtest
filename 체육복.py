def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()

    for L in list(lost):
        if L in list(reserve):
            reserve.remove(L)
            lost.remove(L)

    answer = n - len(lost)

    for L in lost:
        if L == 1:
            if L + 1 in list(reserve):
                reserve.remove(L + 1)
                answer += 1
        elif L == n:
            if L - 1 in list(reserve):
                reserve.remove(L - 1)
                answer += 1
        else:
            if L - 1 in list(reserve):
                reserve.remove(L - 1)
                answer += 1
                continue
            if L + 1 in list(reserve):
                reserve.remove(L + 1)
                answer += 1

    return answer


print(
    solution( 5, [1], [5]))
