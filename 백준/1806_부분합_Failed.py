# DP로 풀면 n^2이 발생하니깐 딴걸로 바꾸자,,,,,,,,,,,

n, s = map(int, input().split())

dp1 = list(map(int, input().split()))
dp2 = [0 for _ in range(n)]
dp3 = [0 for _ in range(n)]

answer = 1
sw = 0

if s in dp1:
    sw = 1

dp2 = dp1[:]

if not sw:
    for i in range(1, n):
        answer += 1
        for k in range(0, n - i):
            dp3[k] = dp2[k] + dp1[k + i]
            if dp3[k] == s:
                sw = 1
                break
        dp2 = dp3[:]
        if sw:
            break

if sw:
    print(answer)

if not sw:
    print(0)
