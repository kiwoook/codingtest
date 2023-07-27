def solution(brown, yellow):

    a = 1
    sw = 0

    while 1:
        for b in range(1, a+1):
            if (brown / 2) + 2 == a + b:
                if (a-2)*(b-2) == yellow:
                    sw = 1
                    break
        if sw == 1:
            break
        a += 1
    return [a, b]


print(solution(24, 24))