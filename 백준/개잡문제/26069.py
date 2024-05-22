import sys

n = int(sys.stdin.readline().rstrip())
dancing_dict = dict()
dancing_dict['ChongChong'] = 1

for _ in range(n):
    per1, per2 = sys.stdin.readline().rstrip().split()
    if dancing_dict.get(per1) == 1 or dancing_dict.get(per2) == 1:
        dancing_dict[per1] = 1
        dancing_dict[per2] = 1

print(len(dancing_dict))