def solution(ingredient):
    answer = 0
    ingredient_len = len(ingredient)
    count = 0
    while count < ingredient_len - 3:
        if ingredient[count:count + 4] == [1, 2, 3, 1]:
            answer += 1
            del ingredient[count:count + 4]
            if count < 4:
                count = 0
            else:
                count -= 3
        else:
            count += 1

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
