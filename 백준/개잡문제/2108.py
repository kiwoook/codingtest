import sys
from collections import Counter

n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

# 산술 평균
print(int(round(sum(num_list) / len(num_list), 0)))

# 중앙값
num_list.sort()

print(num_list[(len(num_list) - 1) // 2])

count_dict = dict(Counter(num_list))
max_count = max(count_dict.values())

mode_list = []
for key, value in count_dict.items():
    if value == max_count:
        mode_list.append(key)

mode_list.sort()

# 최빈값
if len(mode_list) >= 2:
    print(mode_list[1])
else:
    print(mode_list[0])

# 최빈값
print(num_list[-1] - num_list[0])
