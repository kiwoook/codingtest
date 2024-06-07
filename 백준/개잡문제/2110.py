import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

house_list = []
for _ in range(n):
    house_list.append(int(sys.stdin.readline().rstrip()))

house_list.sort()

low, high = 0, max(house_list) + 1

while low < high:
    mid = (low + high) // 2
    cnt = 1

    prev_pos = house_list[0]
    for i in range(1, n):
        distance = house_list[i] - prev_pos
        # 만약 mid 값보다 거리값이 크다면 충족
        if distance >= mid:
            prev_pos = house_list[i]
            cnt += 1

    # 공유기를 많이 설치했다면 거리를 늘려야함
    if cnt >= c:
        low = mid + 1
    else:
        high = mid

print(low - 1)
