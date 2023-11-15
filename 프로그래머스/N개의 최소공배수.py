def lcm(a, b):
    return (a * b) / gcd(a, b)


def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r

    return a


def solution(arr):
    result = arr[0]
    for a in arr[1:]:
        result = lcm(result, a)

    return result
