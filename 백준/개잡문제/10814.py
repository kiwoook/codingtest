import sys

n = int(input())
a = []

for i in range(n):
    tmp = list(sys.stdin.readline().rstrip().split())
    tmp.append(i)
    tmp[0] = int(tmp[0])
    a.append(tmp)

a.sort(key=lambda x: (x[0], x[2]))

for value in a:
    print(*value[0:2])
