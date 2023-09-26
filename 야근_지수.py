import heapq


def solution(n, works):
    q = []
    for work in works:
        heapq.heappush(q, -work)

    for i in range(n):
        print(q)
        x = -heapq.heappop(q) - 1
        heapq.heappush(q, -x)

    return sum(map(lambda x: x ** 2, q))


print(solution(1, [2, 1, 2]))
