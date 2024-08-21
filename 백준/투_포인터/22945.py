import sys

n = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0
left, right = 0, n - 1


while left < right:
    answer = max(answer, (right - left - 1) * min(x[left], x[right]))

    if x[left] < x[right]:
        left += 1
    else:
        right -= 1

print(answer)
