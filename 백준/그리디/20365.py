import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

red_cnt, blue_cnt = 0, 0

flag = 0 if s[0] == 'R' else 1

for char in s:
    if flag == 0 and char == 'R':
        red_cnt += 1
        flag = 1
    if flag == 1 and char == 'B':
        blue_cnt += 1
        flag = 0

answer = 1

sw = 0
if blue_cnt >= red_cnt:
    for char in s:
        if sw == 0 and char == 'R':
            answer += 1
            sw = 1
        elif sw == 1 and char == 'B':
            sw = 0
else:
    for char in s:
        if sw == 0 and char == 'B':
            answer += 1
            sw = 1
        elif sw == 1 and char == 'R':
            sw = 0

print(answer)
