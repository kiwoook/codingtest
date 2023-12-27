# 시간 복잡도는 상관이 없지만 공간 복잡도에서 터져버림

n = int(input())
k = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = (i+1)*(j+1)

b = sum(a, [])
b.sort()

print(b[k-1])

