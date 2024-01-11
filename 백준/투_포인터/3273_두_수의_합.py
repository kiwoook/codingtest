n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

cnt = 0
left, right = 0, n - 1

while left < right:
    hap = a[left] + a[right]
    if hap == x:
        cnt += 1
        right -= 1
    if hap > x:
        right -= 1
    if hap < x:
        left += 1

print(cnt)
