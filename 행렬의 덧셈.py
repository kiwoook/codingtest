def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp = []
        for k in range(len(arr1[0])):
            tmp.append(arr1[i][k] + arr2[i][k])
        answer.append(tmp)


    return answer


print(solution([[1], [2]], [[3], [4]]))
