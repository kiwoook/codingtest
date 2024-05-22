import sys


def find_answer():
    global answer
    prefix_sum = [0 for _ in range(n)]
    prefix_sum[0] = num_list[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + num_list[i]

    for idx in range(1, n - 1):
        hap = prefix_sum[idx - 1] + prefix_sum[-2] - num_list[idx]
        answer = max(answer, hap)


answer = 0
n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 벌통이 안쪽일때 하는 연산
prefix_sum = [0 for _ in range(n)]
prefix_sum[0] = num_list[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + num_list[i]

for idx in range(1, n - 1):
    hap = prefix_sum[idx] - prefix_sum[0] + prefix_sum[-2] - prefix_sum[idx - 1]
    answer = max(answer, hap)

# 벌통이 끝일 떄하는 연산
find_answer()
num_list.reverse()
find_answer()

print(answer)
