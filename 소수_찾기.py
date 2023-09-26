import math
from itertools import permutations


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer_set = set()
    num_list = []

    for number in numbers:
        num_list.append(number)

    comb_list = []
    for i in range(1, len(num_list) + 1):
        comb_list.append(list(permutations(num_list, i)))
    comb_list = sum(comb_list, [])

    int_list = []
    for comb in comb_list:
        int_list.append(int(''.join(comb)))

    for I in int_list:
        if isPrime(I) and I > 1:
            answer_set.add(I)
    return len(answer_set)


print(solution("123"))
