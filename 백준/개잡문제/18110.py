import sys


def k_round(value):
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)


n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
    exit(0)

difficult_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

del_num = int(k_round(n * 0.15))

ans_list = difficult_list[del_num:n - del_num]
print(int(k_round(sum(ans_list) / len(ans_list))))
