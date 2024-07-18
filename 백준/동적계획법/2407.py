import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

factorial = [0 for _ in range(101)]

factorial[0] = 1
factorial[1] = 1

for i in range(2, 101):
    factorial[i] = factorial[i - 1] * i

print(factorial[n] // (factorial[n - m] * factorial[m]))
