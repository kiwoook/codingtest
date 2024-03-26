n = int(input())

sw = 0
for i in range(1, n):
    value = i
    hap = i
    while value != 0:
        hap += value % 10
        value //= 10
    if hap == n:
        print(i)
        sw = 1
        break

if sw == 0:
    print(0)
