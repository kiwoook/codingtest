n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]
answer = [[] for _ in range(n)]

for i in range(n):
    dp[i] = 1
    max_tmp = []
    for j in range(i):
        tmp = []
        if a[i] > a[j]:
            if len(answer[i]) <= len(answer[j]) + 1:
                for v in answer[j]:
                    tmp.append(v)
        if len(max_tmp) < len(tmp):
            max_tmp = tmp
    answer[i] = max_tmp
    answer[i].append(a[i])

max_len_list = max(answer, key=len)

print(len(max_len_list))
print(*max_len_list)
