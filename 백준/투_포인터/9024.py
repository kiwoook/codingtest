import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(map(int, sys.stdin.readline().rstrip().split()))

    left, right = 0, n - 1
    min_key, count = int(1e12), 0

    while left < right:
        value = num_list[left] + num_list[right]
        diff = abs(k - value)

        if diff < min_key:
            min_key = diff
            count = 1
        elif diff == min_key:
            count += 1

        if value < k:
            left += 1
        else:
            right -= 1

    print(count)
