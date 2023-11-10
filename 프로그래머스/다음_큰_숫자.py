# 1의 개수는 유지.
# 0 이 존재하지 않으면 앞의 1을 추가하고 기존 맨 앞은 0

def check_1(num):
    cnt = 0
    for i in num:
        if i == '1':
            cnt += 1
    return cnt


def solution(n):
    compare_cnt = check_1(bin(n)[2::])

    compare_num = n + 1
    while compare_cnt != check_1(bin(compare_num)[2::]):
        compare_num += 1

    return compare_num


print(solution(78))
