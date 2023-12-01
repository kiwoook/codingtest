s = input()
target = input()

n, m = len(s), len(target)

lps, j = [0] * m, 0

for i in range(1,m):
    while j > 0 and target[i] != target[j]:
        j = lps[j - 1]
    if target[i] == target[j]:
        j += 1
    lps[i] = j

# 검색
i = j = 0
sw = 0
while i < n:
    if target[j] == s[i]:
        i += 1
        j += 1
        if j == m:
            print(1)
            sw = 1
            break
    else:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1
if not sw:
    print(0)
