def solution1(numbers):
    answer = []
    for idx, number in enumerate(numbers[:-1]):
        max_num = number

        for k in range(idx + 1, len(numbers) - 1):
            if max_num < numbers[k]:
                max_num = numbers[k]
                break

        if max_num == number:
            answer.append(-1)
        else:
            answer.append(max_num)

    answer.append(-1)

    return answer


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, target in enumerate(numbers):
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        stack.append(idx)

    return answer


print(solution([2, 3, 3, 5]))