a = []
n = 0

# 입력받고 n 최대 값 탐색
for _ in range(5):
    tmp = input()
    n = max(n, len(tmp))
    a.append(list(tmp))
# 빈 값에 스페이스 바 추가
for i in range(5):
    length = len(a[i])
    for _ in range(n - length):
        a[i].append(' ')

answer = []
for i in range(n):
    for k in range(5):
        if a[k][i] != ' ':
            answer.append(a[k][i])

print(''.join(answer))
