import heapq
import sys

num_list = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    heapq.heappush(num_list, int(sys.stdin.readline().rstrip()))

answer = 0

while len(num_list) >= 2:
    v1 = heapq.heappop(num_list)
    v2 = heapq.heappop(num_list)
    heapq.heappush(num_list, v1 + v2)
    answer += v1 + v2

print(answer)