
n = int(input())

answer = 0
hap = 1
left, right = 1, 1

while right <= n:

    if hap == n:
        answer += 1
        hap -= left
        left += 1
    elif hap < n:
        right += 1
        hap += right
    else:
        hap -= left
        left += 1

print(answer)
