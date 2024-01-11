from collections import Counter

n = int(input())
a = list(map(int, input().split()))
x = int(input())
cnt_dict = dict(Counter(a))

print(cnt_dict[x] if x in cnt_dict else "0")
