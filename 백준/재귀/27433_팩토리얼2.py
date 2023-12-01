import sys
sys.setrecursionlimit(2500)


def recur(value):
    global v
    if value == 0:
        return 1
    v *= value
    return recur(value - 1)


n = int(input())

recur(n)
print(v)
