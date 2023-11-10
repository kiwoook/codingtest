import math


def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2

    numer1 = int(numer1 * (denom // denom1))
    numer2 = int(numer2 * (denom // denom2))

    numer = numer1 + numer2
    gcd = math.gcd(numer, denom)

    while gcd != 1:
        numer //= gcd
        denom //= gcd
        gcd = math.gcd(numer, denom)

    return [numer, denom]


print(solution(1, 2, 3, 4))
