def solution(arr1, arr2):
    answer = []

    for idx, a1 in enumerate(arr1):
        tmp = []
        for k in range(len(arr2[0])):
            a2 = list(map(lambda x: x[k], arr2))
            tmp.append(sum([x * y for x, y in zip(a1, a2)]))
        answer.append(tmp)

    return answer


print(solution([[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2], [1, 2], [1, 2], [1, 2]]))
