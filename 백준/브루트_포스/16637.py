# 최적화 ㅈ 까고 우선 구현부터해보자
# 연산자 우선 순위 다 동일
import sys
from itertools import combinations
from collections import deque

def operator(tmp_expression:str):

    stack = []
    for value in tmp_expression:
        if value.isnumeric():
            pass


answer = -2 ** 31
n = int(sys.stdin.readline().rstrip())
exp = sys.stdin.readline().rstrip()

ops_idx_list = [i for i in range(1, n, 2)]
comb_list = []
for choice in range(1, len(ops_idx_list)):
    comb_list.append(list(combinations(ops_idx_list, choice)))
comb_list = sum(comb_list, [])

filter_comb_list = []

for comb in comb_list:
    if len(comb_list) == 1:
        filter_comb_list.append(comb)
    else:
        sw = 0
        for i in range(1, len(comb)):
            if comb[i] - comb[i - 1] <= 2:
                sw = 1
                break

        if sw == 0:
            filter_comb_list.append(comb)

print(filter_comb_list)
