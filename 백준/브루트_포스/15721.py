import sys

a = int(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
# 0 이면 뻔 1이면 데기

# 찾고 싶은 번째
cnt = 0
n = 1  # 회차 저장
idx = 0
while 1:
    order_list = [0, 1, 0, 1] + [0] * (n + 1) + [1] * (n + 1)
    for sound in order_list:
        if sound == k:
            cnt += 1
            if cnt == t:
                print(idx)
                exit(0)

        idx = (idx + 1) % a

    n += 1
