import sys

a = [0 for i in range(31)]

for _ in range(28):
    k = int(sys.stdin.readline().rstrip())
    a[k] = 1

for i in range(1, 31):
    if a[i] == 0:
        print(i)
