import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
left = 0
right = len(arr) - 1
answer = []
min_diff = int(2e12)
while left < right and min_diff != 0:
    diff = arr[right] + arr[left]
    if min_diff >= abs(diff):
        min_diff = abs(diff)
        answer = [arr[left], arr[right]]
    if diff > 0:
        right -= 1
    if diff < 0:
        left += 1


print(*answer)
