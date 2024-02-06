T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    hotel = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    y, x = 0, 0
    cnt = 1
    sw = 0
    for i in range(1, w+1):
        for k in range(1, h+1):
            if cnt == n:
                y = k
                x = i
                sw = 1
                break
            hotel[k][i] = cnt
            cnt += 1
        if sw:
            break

    if x < 10:
        print(str(y) + "0" + str(x))
    else:
        print(str(y) + str(x))

