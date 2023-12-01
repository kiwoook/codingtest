import sys

n = int(input())
stack = []
hap = 0
for i in range(n):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd != 0:
        stack.append(cmd)
        hap += cmd
    if cmd == 0:
        hap -= stack.pop()

print(hap)
