import sys

s = sys.stdin.readline().rstrip()

num = 0
for idx, value in enumerate(s[::-1]):
    num += int(value) * 2 ** idx

print(oct(num)[2:])
