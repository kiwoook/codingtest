def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        if arr[mid] < target:
            start = mid + 1

    return start


n = int(input())
a = list(map(int, input().split()))
answer = []
lis = [a[0]]
dp = [(0, a[0])]

for i in range(1, n):
    if lis[-1] < a[i]:
        lis.append(a[i])
        dp.append((len(lis) - 1, a[i]))
    idx = binary_search(lis, a[i])
    lis[idx] = a[i]
    dp.append((idx, a[i]))

print(len(lis))

last_idx = len(lis) - 1
answer = []

for i in range(len(dp) - 1, -1, -1):
    if dp[i][0] == last_idx:
        answer.append(dp[i][1])
        last_idx -= 1
answer.reverse()
print(*answer)
