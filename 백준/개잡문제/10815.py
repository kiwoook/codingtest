from collections import Counter

n = int(input())

arr = list(map(int, input().split()))

cnt_dict = dict(Counter(arr))

m = int(input())

chk = list(map(int, input().split()))

answer = []
for c in chk:
    if cnt_dict.get(c, 0) != 0:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)