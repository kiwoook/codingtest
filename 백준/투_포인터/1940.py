import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
a = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

answer = 0
left, right = 0, n - 1

while left < right:
    hap = a[left] + a[right]

    if hap < m:
        left += 1
    elif hap == m:
        answer += 1
        right -= 1
    else:
        right -= 1

print(answer)
