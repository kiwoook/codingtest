import math


def is_prime(value):
    if value <= 1:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False

    for v in range(3, int(math.sqrt(value)) + 1, 2):
        if value % v == 0:
            return False

    return True


def check2(value):
    str_value = str(value)

    for i in range(len(str_value) // 2):
        if str_value[i] != str_value[-(i + 1)]:
            return False

    return True


n = int(input())

while not (is_prime(n) and check2(n)):
    n += 1

print(n)
