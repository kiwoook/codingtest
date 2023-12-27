n, m = map(int, input().split())

matrix1 = []

for i in range(n):
    matrix1.append(list(map(int, input().split())))

m, n = map(int, input().split())
matrix2 = []

for i in range(m):
    matrix2.append(list(map(int, input().split())))

matrix = [[0 for _ in range(n)] for _ in range(n)]

# 행렬 곱셈 시행



print(matrix)
