import sys
from itertools import permutations


def str_num(value):
    return ''.join(value)


answer = 0
perm_list = list(map(str_num, permutations([str(i) for i in range(1, 10)], 3)))
n = int(sys.stdin.readline().rstrip())
num_list = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for perm in perm_list:
    flag = 0
    for num, target_strike, target_ball in num_list:
        str_num = str(num)
        strike, ball = 0, 0

        # 우선 맞는 숫자 판단
        for i in range(3):
            if str_num[i] in perm:
                ball += 1

        # 자리수 맞는 지 판단
        for i in range(3):
            if str_num[i] == perm[i]:
                strike += 1
                ball -= 1

        if target_strike == strike and target_ball == ball:
            flag += 1

    if flag == n:
        answer += 1

print(answer)
