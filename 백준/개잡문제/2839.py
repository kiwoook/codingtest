n = int(input())
answer = int(1e9)
x = n

for i in range(0, n // 5 + 1):
    tmp = i
    x = n - 5 * i
    if x % 3 == 0:
        tmp += x // 3
        answer = min(answer, tmp)

print(answer if answer != int(1e9) else -1)
