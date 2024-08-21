import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().rstrip().split())
sushi_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt_dict = defaultdict(int)
cnt = 0

for i in range(k):
    if cnt_dict[sushi_list[i]] == 0:
        cnt += 1
    cnt_dict[sushi_list[i]] += 1

max_sushi = cnt + 1 if cnt_dict[c] == 0 else cnt

for i in range(1, n):
    left_sushi = sushi_list[i - 1]
    cnt_dict[left_sushi] -= 1
    if cnt_dict[left_sushi] == 0:
        cnt -= 1

    right_sushi = sushi_list[(i + k - 1) % n]
    if cnt_dict[right_sushi] == 0:
        cnt += 1
    cnt_dict[right_sushi] += 1

    # 쿠폰 초밥 포함 여부 계산
    max_sushi = max(max_sushi, cnt + 1 if cnt_dict[c] == 0 else cnt)

print(max_sushi)
