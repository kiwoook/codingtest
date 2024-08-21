import sys

n = int(sys.stdin.readline().rstrip())
h = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

answer = int(1e12)

for i in range(n):
    for j in range(i + 3, n):
        left, right = i + 1, j - 1

        while left < right:
            value = (h[i] + h[j]) - (h[left] + h[right])
            answer = min(answer, abs(value))

            if value < 0:
                right -= 1
            else:
                left += 1

print(answer)
