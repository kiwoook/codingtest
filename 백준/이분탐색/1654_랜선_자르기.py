import sys


def hap(l_list, v):
    cnt = 0

    for l in l_list:
        cnt += l // v

    return cnt


n, k = map(int, input().split())

lan_list = []
for i in range(n):
    lan_list.append(int(sys.stdin.readline().strip()))

start, end = 1,  max(lan_list)

result = 0

while start <= end:
    mid = (start + end) // 2

    value = hap(lan_list, mid)

    if value >= k:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
