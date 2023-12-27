import heapq
import sys

n = int(input())

heap = []

input_list = []
for i in range(n):
    input_list.append(int(sys.stdin.readline().strip()))

for num in input_list:
    if num == 0:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
