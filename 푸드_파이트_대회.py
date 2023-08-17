def solution(food):
    for idx, v in enumerate(food):
        if idx > 0 and v % 2 == 1:
            food[idx] = v - 1
    len_food = sum(food)
    list_food = [0]*len_food

    pointer = 0
    for idx, v, in enumerate(food):
        if idx >= 1:
            v = v // 2
            for i in range(v):
                list_food[pointer] = idx
                list_food[-(1+pointer)] = idx
                pointer += 1
    list_food = map(str, list_food)
    return ''.join(list_food)


print(solution([1, 3, 4, 6]))
