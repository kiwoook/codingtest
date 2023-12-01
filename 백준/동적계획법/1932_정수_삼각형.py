import sys

n = int(input())

tri_list = [[0 for _ in range(n)] for i in range(n)]

for i in range(n):
    input_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for idx, value in enumerate(input_list):
        tri_list[i][idx] = value

for i in range(1, n):
    for k in range(i+1):
        if k == 0:
            tri_list[i][0] += tri_list[i-1][0]
        elif k == i:
            tri_list[i][k] += tri_list[i-1][k-1]
        else:
            tri_list[i][k] += max(tri_list[i-1][k], tri_list[i-1][k-1])

print(max(tri_list[-1]))
