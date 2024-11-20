import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def checking(outer_s, inner_s):
    outer_len = len(outer_s)
    inner_len = len(inner_s)

    lcm_value = lcm(outer_len, inner_len)

    outer_s = outer_s * (lcm_value // outer_len)
    inner_s = inner_s * (lcm_value // inner_len)

    return 1 if outer_s == inner_s else 0


s = input()
t = input()

if len(s) >= len(t):
    print(checking(s, t))
else:
    print(checking(t, s))
