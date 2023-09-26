def solution(arr1, arr2):
    answer = []
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    n, m = len(arr1), len(arr1[0])
    for i in range(n):
        tmp = []
        for k in range(m):
            hap = 0
            for j in range(m):
                hap += arr1[i][j] * arr2[j][k]
            tmp.append(hap)
        answer.append(tmp)

    for k in range(n)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution( [[1,2,3,4], [1,2,3,4]],[[1,2], [1,2], [1,2], [1,2]]  ))