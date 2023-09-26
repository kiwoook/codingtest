def solution(expression):
    max_result = 0
    priors = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]

    number_list = []
    operator_list = []
    tmp = ""
    for exp in expression:
        if exp.isnumeric():
            tmp += exp
        if exp == '*' or exp == '+' or exp == '-':
            number_list.append(int(tmp))
            tmp = ""
            operator_list.append(exp)
    number_list.append(int(tmp))

    for prior in priors:
        use_operator = operator_list.copy()
        use_number = number_list.copy()
        value = 0
        for i in range(3):
            while prior[i] in use_operator:
                idx = use_operator.index(prior[i])
                if prior[i] == '*':
                    value = use_number[idx] * use_number[idx + 1]
                if prior[i] == '-':
                    value = use_number[idx] - use_number[idx + 1]
                if prior[i] == '+':
                    value = use_number[idx] + use_number[idx + 1]
                use_operator.pop(idx)
                use_number[idx:idx + 2] = [value]
        max_result = max(abs(value), max_result)
    return max_result


print(solution("100-200*300-500+20"))
