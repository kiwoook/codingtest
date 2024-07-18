n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
hap = 0
answer = 0

while right < n:
    if hap < m:
        hap += a[right]
        right += 1
    elif hap == m:
        answer += 1
        hap -= a[left]
        left += 1
    else:
        hap -= a[left]
        left += 1

if hap == m:
    answer += 1

print(answer)