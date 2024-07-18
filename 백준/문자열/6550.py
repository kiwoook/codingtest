import sys

while True:
    try:
        s, t = sys.stdin.readline().rstrip().split()

        idx = 0
        for t_char in t:
            if idx == len(s):
                break
            if s[idx] == t_char:
                idx += 1

        if idx == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break
