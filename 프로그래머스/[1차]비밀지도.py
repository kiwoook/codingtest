def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []

    for value in arr1:
        value_list = list(bin(value))[2:]
        while len(value_list) < n:
            value_list.insert(0, '0')
        map1.append(value_list)

    for value in arr2:
        value_list = list(bin(value))[2:]
        while len(value_list) < n:
            value_list.insert(0, '0')
        map2.append(value_list)

    for i in range(n):
        str_answer = ''
        for k in range(n):
            if map1[i][k] == '0' and map2[i][k] == '0':
                str_answer += ' '
            else:
                str_answer += '#'
        answer.append(str_answer)

    return answer






print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
