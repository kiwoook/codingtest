import sys

hap = 0
n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

for idx, char in enumerate(s):
    hap += (ord(char) - ord('a') + 1) * 31 ** idx

print(hap % 1234567891)
