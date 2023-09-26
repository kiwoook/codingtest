def solution(s):
    s = list(s)
    total_remove = 0
    cnt = 0
    while 1:
        remove_cnt = 0
        for v in s:
            if v == '0':
                remove_cnt += 1
        s = list(bin(len(s) - remove_cnt)[2:])
        cnt += 1
        total_remove += remove_cnt
        if len(s) == 1 and s[0] == '1':
            break

    return [cnt, total_remove]

print(solution("01110"))