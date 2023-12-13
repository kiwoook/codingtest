import sys

n = int(input())

conference = []

for i in range(n):
    conference.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

conference.sort(key=lambda x: (x[1],x[0]))

start, end = conference[0]
answer = 1

for s, e in conference[1:]:
    if end <= s:
        end = e
        start = s
        answer += 1

print(answer)
