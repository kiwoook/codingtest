import sys

name_dict = dict()
answer = []

n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    name_dict[name] = 1
for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name_dict.get(name) is not None:
        answer.append(name)

answer.sort()
print(len(answer))

for n in answer:
    print(n)
