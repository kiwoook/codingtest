import sys
from collections import deque

current_channel = 100
min_cnt = [int(1e9) for _ in range(2000001)]

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

out_of_order_btn = []
if m != 0:
    out_of_order_btn = list(sys.stdin.readline().rstrip().split())

len_n = len(str(n))
if len_n == 1 or len_n == 2:
    start = 0
    end = 1000
else:
    start = ['1'] + ['0' for _ in range(len_n - 2)]
    start = int(''.join(start))
    end = ['1'] + ['9' for _ in range(len_n)]
    end = int(''.join(end))

min_cnt[n] = abs(n - current_channel)

q = deque([n])

for value in range(start, end + 1):
    str_value = str(value)
    sw = 0
    for btn in out_of_order_btn:
        if btn in str_value:
            sw = 1
            break
    if sw == 0:
        min_cnt[value] = min(min_cnt[value], len(str_value) + abs(value - n))

print(min(min_cnt))
