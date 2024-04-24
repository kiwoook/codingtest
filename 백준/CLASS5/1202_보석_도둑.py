import heapq
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

gems = []
bags = []
heap = []

for _ in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    gems.append((m, v))
for _ in range(k):
    bags.append(int(sys.stdin.readline().rstrip()))

gems.sort()
bags.sort()

answer = 0

tmp = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        answer += -heapq.heappop(tmp)
print(answer)
