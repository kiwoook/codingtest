n, s = map(int, input().split())

arr = list(map(int, input().split()))

# sum쓰면 시간 복잡도 늘어난다~

total = arr[0]
left = 0
right = 0
sw = 0
min_len = 1e9
while left <= right:
    if total < s and right == n-1:
        total -= arr[left]
        left += 1
        continue
    if total < s:
        right += 1
        total += arr[right]
    else:
        if min_len > right - left + 1:
            min_len = right - left + 1
        sw = 1
        total -= arr[left]
        left += 1

if sw:
    print(min_len)
else:
    print(0)
