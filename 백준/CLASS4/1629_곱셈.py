def power(k):
    if k == 1:
        return a % c
    else:
        k = power(k // 2)
        if k % 2 == 0:
            return (k * k) % c
        else:
            return (a * k * k) % c


a, b, c = map(int, input().split())
print(power(b))
