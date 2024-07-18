n, k = map(int, input().split())
s = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
answer = 0
while right < n:
    if cnt > k:
        if s[left] % 2 == 1:
            cnt -= 1
        left += 1

    else:
        if s[right] % 2 == 1:
            cnt += 1
        right += 1
    if cnt <= k:
        answer = max(answer, right - left - cnt)

print(answer)
