def check(value):
    global answer_list
    group_cnt = 1
    total, total_cnt = 0, 0
    cnt_list = []

    for num in num_list:
        if total + num <= value:
            total += num
            total_cnt += 1
        else:
            cnt_list.append(total_cnt)
            group_cnt += 1
            if group_cnt > m:
                return False
            total, total_cnt = num, 1
    cnt_list.append(total_cnt)

    # 숫자 하나가 2보다 크다면 쪼개버려
    # 그리고 나머지는 그대로 넣어

    while len(cnt_list) != m:
        sw = 0
        tmp_list = []
        for cnt_num in cnt_list:
            if sw == 0 and cnt_num >= 2:
                tmp_list.append(cnt_num - 1)
                tmp_list.append(1)
                sw = 1
            else:
                tmp_list.append(cnt_num)
        cnt_list = tmp_list[:]

    answer_list = cnt_list[:]

    return True


# 그룹의 개수를 맞추어야 함
answer_list = []

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

left, right = max(num_list), sum(num_list)

while left < right:
    mid = (left + right) // 2

    if check(mid):
        right -= 1
    else:
        left += 1

print(right)

while len(answer_list) != 0:
    answer_list.append(0)
print(*answer_list)
