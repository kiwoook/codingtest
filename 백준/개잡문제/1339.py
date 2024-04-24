import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
max_answer = 0
alphabet_dict = defaultdict(int)

word_list = []

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    word_list.append(s)
    for i in range(len(s)):
        # 최대 위치로 정렬시킨다.
        reverse_idx = len(s) - 1 - i
        alphabet_dict[s[reverse_idx]] += 10 ** i

num_order_list = []

# 튜플로 정렬시켜보자.
for key, value in alphabet_dict.items():
    num_order_list.append((key, value))

num_order_list.sort(key=lambda x: x[1], reverse=True)

number = 9
answer = 0
for num, value in num_order_list:
    answer += value * number
    number -= 1

print(answer)
