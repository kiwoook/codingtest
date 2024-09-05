s = list(input().strip())
len_s, answer = len(s), 0
L_cnt, R_cnt = [], []

# 왼쪽 개수
cnt = 0
for i in range(len_s):
    if s[i] == 'K':
        cnt += 1
    else:
        L_cnt.append(cnt)

# 오른쪽 개수
cnt = 0
for i in range(len_s - 1, -1, -1):
    if s[i] == 'K':
        cnt += 1
    else:
        R_cnt.append(cnt)

R_cnt.reverse()

left, right = 0, len(L_cnt) - 1
while left <= right:
    answer = max(answer, right - left + 1 + 2 * min(L_cnt[left], R_cnt[right]))
    if L_cnt[left] > R_cnt[right]:
        right -= 1
    else:
        left += 1

print(answer)
