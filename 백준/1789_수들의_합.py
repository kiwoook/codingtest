import sys
s = int(sys.stdin.readline().rstrip())
total = 0
i = 0
while total <= s:
    i += 1
    total = (i / 2) * (1 + i)

print(i - 1)
