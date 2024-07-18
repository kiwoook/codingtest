import sys

n = int(sys.stdin.readline().rstrip())

a_list, b_list, c_list, d_list = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

a_list.sort()
b_list.sort()
c_list.sort()
d_list.sort()

print(a_list)
print(b_list)
print(c_list)
print(d_list)
