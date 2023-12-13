import sys


def sum_arr(y1, x1, y2, x2):
    hap = 0

    for j in range(y1, y2 + 1):
        if x1 == 0:
            hap += prefix_arr[j][x2]
        else:
            hap += prefix_arr[j][x2] - prefix_arr[j][x1 - 1]

    return hap


n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

prefix_arr = [[i[0]] for idx, i in enumerate(arr)]

# 누적합 구현
for i in range(n):
    for k in range(1, n):
        prefix_arr[i].append(prefix_arr[i][k - 1] + arr[i][k])

for i in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())
    print(sum_arr(y1 - 1, x1 - 1, y2 - 1, x2 - 1))
