import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    phone_num_list = []
    flag = 0
    phone_dict = dict()
    for _ in range(n):
        phone_num_list.append(sys.stdin.readline().rstrip())

    for phone_num in phone_num_list:
        phone_dict[phone_num] = True

    for phone_num in phone_num_list:
        for i in range(1, len(phone_num)):
            if phone_num[0:i] in phone_dict:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
        print("YES")
    else:
        print("NO")
