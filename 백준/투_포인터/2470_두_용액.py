import sys

n = int(input())
a = list(map(int, sys.stdin.readline().rstrip().split()))
min_diff = int(2e9)

a.sort()

left, right = 0, n - 1
answer = [a[left], a[right]]

while left < right:
    hap = a[left] + a[right]
    if abs(hap) <= abs(min_diff):
        min_diff = abs(hap)
        answer = [a[left], a[right]]
        if min_diff == 0:
            break

    if hap < 0:
        left += 1
    else:
        right -= 1

print(*answer)
