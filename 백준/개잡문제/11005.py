n, b = map(int, input().split())

if n == 0:
    print("0")
    exit(0)

answer = []

while n > 0:
    v = n % b
    if v >= 10:
        answer.append(chr(v - 10 + ord('A')))
    else:
        answer.append(str(v))
    n //= b

answer.reverse()
print(''.join(answer))