import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        else:
            print(s)
except:
    print(end='')
