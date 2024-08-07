import heapq
import sys

n = int(sys.stdin.readline().rstrip())
crane_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
m = int(sys.stdin.readline().rstrip())
box_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

if crane_list[0] < box_list[0]:
    print(-1)
    exit(0)

heap = []
for box in box_list:
    heapq.heappush(heap, -box)

time = 0

while heap:
    time += 1
    tmp = []
    for crane in crane_list:
        while heap:
            box = -heapq.heappop(heap)
            if box <= crane:
                break
            tmp.append(box)

    for box in tmp:
        heapq.heappush(heap, -box)

print(time)
