n, k = map(int, input().split())
number_list = list(map(int, input().split()))
cnt = [0 for _ in range(100001)]
answer = 0

left = 0
right = 0

while right < n:
    if cnt[number_list[right]] < k:
        cnt[number_list[right]] += 1
        right += 1
    else:
        cnt[number_list[left]] -= 1
        left += 1

    answer = max(answer, right - left)

print(answer)