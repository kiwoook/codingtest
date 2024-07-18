import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
file_dict = defaultdict(int)

for _ in range(n):
    file_name = sys.stdin.readline().rstrip().split('.')

    file_dict[file_name[1]] += 1

file_name_list = sorted(file_dict.keys())

for file_name in file_name_list:
    print(file_name, file_dict[file_name])
