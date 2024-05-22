# 다 비교하고 이긴 숫자대로 정렬
import sys

rank_dict = dict()
per_list = []
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    rank_dict[i] = 0

for _ in range(n):
    per_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n - 1):
    for k in range(i + 1, n):
        if per_list[i][0] > per_list[k][0] and per_list[i][1] > per_list[k][1]:
            rank_dict[k] += 1
        elif per_list[i][0] < per_list[k][0] and per_list[i][1] < per_list[k][1]:
            rank_dict[i] += 1

rank_list = []

answer = []
for key, value in rank_dict.items():
    answer.append(value + 1)

print(*answer)
