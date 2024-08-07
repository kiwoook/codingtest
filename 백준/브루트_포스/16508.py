import sys
from collections import defaultdict
from itertools import combinations

answer = float('inf')
t = list(sys.stdin.readline().rstrip())
target_dict = defaultdict(int)
n = int(sys.stdin.readline().rstrip())

for char in t:
    target_dict[char] += 1

book_list = []

for idx in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    s = []

    for char in b:
        if char in t:
            s.append(char)

    if len(s) > 0:
        book_list.append((int(a), s))

for choice in range(1, len(book_list) + 1):

    comb_list = list(combinations(book_list, choice))
    for comb in comb_list:
        total = 0
        total_dict = defaultdict(int)
        for price, alpha in comb:
            total += price
            for char in alpha:
                total_dict[char] += 1

        sw = 0
        for key, value in target_dict.items():
            if total_dict[key] < value:
                sw = 1
                break

        if sw == 0:
            answer = min(answer, total)

print(answer if answer != float('inf') else -1)
