import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    ipt = list(map(int, sys.stdin.readline().rstrip().split()))
    test_num = ipt[0]
    child_list = ipt[1:]
    cnt = 0
    idx = 1
    while idx < len(child_list):
        if child_list[idx - 1] > child_list[idx]:
            child_list[idx - 1], child_list[idx] = child_list[idx], child_list[idx - 1]
            cnt += 1
            if idx != 1:
                idx -= 1
        else:
            idx += 1

    print(test_num, cnt)
