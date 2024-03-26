import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    str_input = sys.stdin.readline().rstrip()[1:-1]
    str_list = []

    if len(str_input) > 0:
        if str_input.find(',') != -1:
            str_list = list((str_input.split(',')))
        else:
            str_list.append(str_input)
    q = deque(str_list)
    answer_sw = 1
    sw = 0
    for v in cmd:
        if v == 'R':
            if sw == 0:
                sw = 1
            else:
                sw = 0
        if v == 'D':
            if len(q) == 0:
                answer_sw = 0
                print("error")
                break
            elif sw == 0:
                q.popleft()
            elif sw == 1:
                q.pop()
    if answer_sw != 0:
        if sw == 1:
            q.reverse()
            print('[' + ','.join(q) + ']')
        else:
            print('[' + ','.join(q) + ']')
