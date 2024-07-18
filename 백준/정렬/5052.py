import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    start_digit_list = [[] for _ in range(10)]
    flag = 0
    for _ in range(n):
        v = sys.stdin.readline().rstrip()

        start_digit_list[int(v[0])].append(v)

    for digit_phone_num_list in start_digit_list:
        digit_phone_num_list.sort(key=lambda x: len(x))
        if len(digit_phone_num_list) < 2:
            continue

        for idx, phone_num in enumerate(digit_phone_num_list):
            for compare_phone_num in digit_phone_num_list[idx+1:]:
                if phone_num == compare_phone_num[:len(phone_num)]:
                    flag = 1
                    break
            if flag == 1:
                break

        if flag == 1:
            break

    if flag == 0:
        print("YES")
    else:
        print("NO")
