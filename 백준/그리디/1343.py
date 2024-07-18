dp = [""] * 51

for num in range(2, 51):
    idx = num
    tmp = ''
    count_AAAA = num // 4
    remainder = num % 4

    if remainder % 2 != 0:
        continue

    tmp += 'AAAA' * count_AAAA
    tmp += 'BB' * (remainder // 2)

    dp[idx] = tmp

arr = []
cnt = 0

s = input()

for char in s:
    if char == 'X':
        cnt += 1
    else:
        if cnt != 0:
            arr.append(cnt)
        arr.append('.')
        cnt = 0

if cnt != 0:
    arr.append(cnt)

answer = ''

for a in arr:
    if a != '.' and dp[a] == "":
        print(-1)
        exit(0)
    answer += (dp[a] if a != '.' else '.')

print(answer)
