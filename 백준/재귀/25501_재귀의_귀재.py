import sys

sys.setrecursionlimit(2500)
v = 0


def recur(string, start, end):
    global v
    v += 1
    if start >= end:
        return 1
    elif string[start] != string[end]:
        return 0
    else:
        return recur(string, start + 1, end - 1)


n = int(input())

for i in range(n):
    v = 0
    s = sys.stdin.readline().rstrip()
    print("%d %d" % (recur(s, 0, len(s) - 1), v))
