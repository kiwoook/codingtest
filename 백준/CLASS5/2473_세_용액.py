import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

min_diff = int(3e12)
answer = []

for mid in range(1, n - 1):
    left = 0
    right = n - 1
    while left < mid < right and min_diff != 0:
        diff = a[left] + a[mid] + a[right]
        if min_diff >= abs(diff):
            min_diff = abs(diff)
            answer = [a[left], a[mid], a[right]]
        if diff > 0:
            right -= 1
        if diff < 0:
            left += 1

print(*answer)
