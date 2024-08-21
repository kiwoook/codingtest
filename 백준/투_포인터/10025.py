import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
pail_list = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)], key=lambda x: x[1])
answer = pail_list[0][0]
start, end, hap = 0, 0, 0

while start <= end < n:
    if pail_list[end][1] - pail_list[start][1] <= 2 * k:
        hap += pail_list[end][0]
        answer = max(answer, hap)
        end += 1
    else:
        hap -= pail_list[start][0]
        start += 1

print(answer)
