def is_number(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


def separate_numbers_and_letters(s):
    result = []
    current_num = ""

    for char in s:
        if is_number(char):
            current_num += char
        else:
            if current_num:
                result.append(int(current_num))
                current_num = ""
            if char:
                result.append(char)

    return result


def solution(dartResult):
    list_dart = separate_numbers_and_letters(dartResult)
    sum_dart = []

    print(list_dart)

    for idx, dart in enumerate(list_dart):
        if list_dart[idx] == 'S':
            list_dart[idx - 1] = int(list_dart[idx - 1])
        if list_dart[idx] == 'D':
            list_dart[idx - 1] = int(list_dart[idx - 1]) ** 2
        if list_dart[idx] == 'T':
            list_dart[idx - 1] = int(list_dart[idx - 1]) ** 3

    for dart in list_dart:
        if dart == 'S' or dart == 'D' or dart == 'T':
            pass
        else:
            sum_dart.append(dart)

    while '*' in sum_dart or '#' in sum_dart:
        for idx, dart in enumerate(sum_dart):
            if dart == '*':
                sum_dart[idx - 1] = int(sum_dart[idx - 1]) * 2
                if idx >= 2:
                    sum_dart[idx - 2] *= 2
                sum_dart.pop(idx)
                break
            if dart == '#':
                sum_dart[idx - 1] = int(sum_dart[idx - 1]) * -1
                sum_dart.pop(idx)
                break

    print(sum_dart)
    return sum(sum_dart)


print(solution("1D2S#10S"))
