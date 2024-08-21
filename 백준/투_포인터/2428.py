import sys

n = int(sys.stdin.readline().rstrip())
file_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

answer = 0
left, right = 0, 0

while left < n:
    while right < n and file_list[left] >= 0.9 * file_list[right]:
        right += 1
    gap = right - left - 1
    answer += gap
    left += 1

print(answer)
