def recur(n):
    if n < 0:
        return
    if n == 0:
        return 0
    if n == 1:
        return 1

    return recur(n - 1) + recur(n - 2)


k = int(input())

print(recur(k))
