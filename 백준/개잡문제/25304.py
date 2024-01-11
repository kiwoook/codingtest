import sys

total = int(input())
n = int(input())
check_sum = 0
for _ in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    check_sum += a * b


if check_sum == total:
    print("Yes")
else:
    print("No")