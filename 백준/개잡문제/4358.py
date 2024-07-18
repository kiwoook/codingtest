import sys
from collections import defaultdict

cnt_dict = defaultdict(int)
total = 0
while True:
    s = sys.stdin.readline().rstrip()
    if not s:
        break
    cnt_dict[s] += 1
    total += 1

name_list = sorted(cnt_dict.keys())

for name in name_list:
    print("%s %.4f" % (name, cnt_dict[name] / total * 100))
