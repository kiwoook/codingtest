import sys

white = 0
blue = 0


def check(start_y, start_x, length):
    # 하얀색 종이인지 체크
    sw = True
    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            if paper[a][b] == 1:
                sw = False
                break
        if not sw:
            break
    if sw:
        return 0

    sw = True

    # 파란색 종이인지 체크
    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            if paper[a][b] == 0:
                sw = False
                break
        if not sw:
            break
    if sw:
        return 1

    # 하얀색도 파란색도 아님.
    return -1


def recur(start_y, start_x, length):
    global white, blue

    if length == 0:
        return

    value = check(start_y, start_x, length)

    if value == -1:
        # 4분할
        recur(start_y, start_x, length // 2)
        recur(start_y, start_x + length // 2, length // 2)
        recur(start_y + length // 2, start_x, length // 2)
        recur(start_y + length // 2, start_x + length // 2, length // 2)
    if value == 0:
        white += 1
        return
    if value == 1:
        blue += 1
        return


n = int(input())

paper = []

for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

recur(0, 0, n)

print(white)
print(blue)
