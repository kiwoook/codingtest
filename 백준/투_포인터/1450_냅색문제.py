N, C = map(int, input().split())
weights = list(map(int, input().split()))
left = 0
right = N - 1
cnt = 0
a = []

for weight in weights:
    a.append(0)
    a.append(weight)

a.sort()

total = sum(a[left:right + 1])

while left < right:
    if total <= C:
        cnt += 1
        if right + 1 == len(a):
            if left < len(a):
                total -= a[left]
                left += 1
        elif right + 1 < len(a):
            right += 1
            total += a[right]
    else:
        if left + 1 < len(a):
            total -= a[left]
            left += 1


print(cnt)
