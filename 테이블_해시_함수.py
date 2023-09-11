def solution(data, col, row_begin, row_end):
    m = len(data[0])
    xor_list = []

    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i in range(row_begin - 1, row_end):
        tmp = 0
        for k in range(m):
            tmp += (data[i][k] % (i + 1))
        xor_list.append(tmp)
    answer = xor_list[0]

    for v in xor_list[1:]:
        answer ^= v

    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))
