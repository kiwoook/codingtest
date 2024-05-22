n, b = input().split()

b = int(b)
answer = 0
gop = 0
for i in range(len(n) - 1, -1, -1):
    if '0' <= n[i] <= '9':
        answer += int(n[i]) * (b ** gop)
    else:
        tmp = ord(n[i]) - ord('A') + 10
        answer += tmp * (b ** gop)
    gop += 1

print(answer)
