import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
answer = 0

for hour in range(0, n+1):
    for minute in range(0, 60):
        for sec in range(0, 60):
            time = "{:02}{:02}{:02}".format(hour, minute, sec)
            if str(k) in time:
                answer += 1

print(answer)