# 0 1 10 11 100 101
# 문자로 합쳐서 t를 넘어가면 그만하도록
# 우선 만들어내고 추출하는 방법으로 가자

def number(n, arg):
    num = ''



    while arg >= 1:
        if arg % n >= 10:
            num = str(chr(arg % n - 10 + ord('A'))) + num
        else:
            num = str(arg % n) + num
        arg //= n

    return num


def solution(n, t, m, p):
    answer = ''
    num_collect = '0'
    for i in range(t*n*m):
        num_collect += number(n, i)

    for i in range(t):
        answer += num_collect[p - 1 + m * i]

    return answer


print(solution(16, 100, 2, 1))
print(solution(2, 4, 2, 1))
