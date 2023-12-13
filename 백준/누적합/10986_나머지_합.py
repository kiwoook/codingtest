n, m = map(int, input().split())

arr = list(map(int, input().split()))

prefix_arr = [0 for _ in range(len(arr))]
prefix_arr[0] = arr[0]

hap = 0
cnt = [0 for _ in range(1001)]

for i in range(n):
    hap += arr[i]
    cnt[hap % m] += 1

ans = 0

for i in range(0, 1001):
    ans += cnt[i] * (cnt[i] - 1) / 2

print(int(cnt[0] + ans))
