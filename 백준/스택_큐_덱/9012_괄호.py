import sys

n = int(input())
for i in range(n):
    ps = sys.stdin.readline().rstrip()
    check_cnt = 0
    sw = 0
    for s in ps:
        if s == "(":
            check_cnt += 1
        else:
            check_cnt -= 1
            if check_cnt < 0:
                sw = 1
                break
    if sw == 1:
        print("NO")
    elif check_cnt == 0:
        print("YES")
    else:
        print("NO")
