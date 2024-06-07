import sys

n = int(sys.stdin.readline().rstrip())

info_list = []
people = 0

for _ in range(n):
    x, a = map(int, sys.stdin.readline().rstrip().split())
    info_list.append((x, a))
    people += a
info_list.sort(key=lambda v: v[0])

cnt = 0
for distance, p_cnt in info_list:
    cnt += p_cnt
    if cnt >= people / 2:
        print(distance)
        break

