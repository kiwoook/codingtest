a, b = map(int, input().split())
cnt = 0
sw = 0
while a <= b:
    cnt += 1

    if a == b:
        sw = 1
        print(cnt)

    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break

if not sw:
    print("-1")
