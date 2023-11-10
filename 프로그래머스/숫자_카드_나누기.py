def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    # arrayA의 최대공약수를 계산한다. 단, 최대 공약수가 1이 나오는 순간 중단
    result1 = arrayA[0]
    for a in arrayA[1:]:
        result1 = find_gcd(result1, a)
        if result1 == 1:
            break

    result2 = arrayB[0]
    for b in arrayB[1:]:
        result2 = find_gcd(result2, b)
        if result2 == 1:
            break

    if result2 > result1:
        sw = 0
        for a in arrayA:
            if a % result2 == 0:
                sw = 1
        if sw == 0:
            return result2
    else:
        sw = 0
        for b in arrayB:
            if b % result1 == 0:
                sw = 1
        if sw == 0:
            return result1

    return 0


print(solution([14, 35, 119], [18, 30, 102]))
