import sys

n = int(input())
atm = list(map(int, sys.stdin.readline().rstrip().split()))
hap = 0

atm.sort()

for i in range(n):
    hap += sum(atm[:i+1])

print(hap)
