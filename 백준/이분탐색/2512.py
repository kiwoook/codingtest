import sys


def total(target):
    hap = 0
    for num in num_list:
        if num >= target:
            hap += target
        else:
            hap += num
    return hap


n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

if sum(num_list) <= m:
    print(max(num_list))
else:
    left = 0
    right = max(num_list)

    while left <= right:
        mid = (left + right) // 2
        if total(mid) <= m:
            left = mid + 1
        else:
            right = mid - 1

    print(right)
