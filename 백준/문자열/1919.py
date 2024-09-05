from collections import Counter

s1 = input()
s2 = input()

s1_cnt = Counter(s1)
s2_cnt = Counter(s2)

common_count = sum((s1_cnt & s2_cnt).values())

result = len(s1) + len(s2) - 2 * common_count

print(result)
