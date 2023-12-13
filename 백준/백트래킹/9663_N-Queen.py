import sys

sys.setrecursionlimit(2500)

cnt = 0

# TMP의 인덱스는 x좌표를 의미하고 값은 Y를 의미한다.

def nqueen(col):
    global cnt, tmp
    if col == n:
        cnt += 1
        return
    for k in range(n):
        check = True
        for j in range(col):
            tmp[col] = k
            if tmp[j] == tmp[col] or abs(j - col) == abs(tmp[j] - tmp[col]):
                check = False
                break
        if check:
            nqueen(col + 1)


n = int(input())
tmp = [0 for _ in range(n + 1)]

for i in range(n):
    tmp[0] = i
    nqueen(1)

print(cnt)
