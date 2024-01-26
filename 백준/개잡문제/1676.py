import math

n = int(input())

value = str(math.factorial(n))

cnt = 0

for v in value[::-1]:
    if v == '0':
        cnt += 1
    else:
        break

print(cnt)
