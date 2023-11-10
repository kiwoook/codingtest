def solution(n):
    s = ''
    while n > 0:
        if n % 3 == 0:
            s = '4' + s
            n -= 1
        else:
            s = str(n % 3) + s
        n //= 3
    return s