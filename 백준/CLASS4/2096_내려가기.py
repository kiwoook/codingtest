import sys
from collections import deque

dx = [-1, 0, 1]
n = int(sys.stdin.readline().rstrip())

min_dp_q = deque([])
max_dp_q = deque([])

for i in range(n):
    tmp_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    max_tmp_list = [x for x in tmp_lst]
    min_tmp_list = [x for x in tmp_lst]

    if i == 0:
        min_dp_q.append(tmp_lst)
        max_dp_q.append(tmp_lst)
    else:
        min_dp = min_dp_q.popleft()
        max_dp = max_dp_q.popleft()
        for x in range(3):
            max_value = 0
            min_value = int(1e9)
            for j in range(3):
                nx = x + dx[j]
                if 0 <= nx < 3:
                    min_value = min(min_value, min_dp[nx])
                    max_value = max(max_value, max_dp[nx])
            min_tmp_list[x] += min_value
            max_tmp_list[x] += max_value
        max_dp_q.append(max_tmp_list)
        min_dp_q.append(min_tmp_list)

print(max(max_dp_q.pop()), min(min_dp_q.pop()))
