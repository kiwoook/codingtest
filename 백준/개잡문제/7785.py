import sys

in_dict = dict()
name_list = []

n = int(input())

for _ in range(n):
    name, cmd = sys.stdin.readline().rstrip().split()
    if cmd == 'enter':
        in_dict[name] = 1
    else:
        del in_dict[name]

for name in in_dict.keys():
    name_list.append(name)

name_list.sort(reverse=True)

for name in name_list:
    print(name)


