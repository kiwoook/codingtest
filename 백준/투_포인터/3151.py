from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

answer = 0
a.sort()

for idx in range(n - 2):
    left = idx + 1
    right = n - 1

    while left < right:
        if a[idx] + a[left] + a[right] > 0:
            right -= 1
        else:
            if a[idx] + a[left] + a[right] == 0:
                if a[left] == a[right]:
                    answer += right - left
                else:
                    left_idx = bisect_left(a, a[right])
                    answer += right - left_idx + 1
            left += 1

print(answer)
