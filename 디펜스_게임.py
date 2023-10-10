import heapq


def solution(n, k, enemy):
    heap = []

    if len(enemy) <= k:
        return len(enemy)

    for rnd, value in enumerate(enemy):

        n -= value
        print(rnd, n, k, heap)
        heapq.heappush(heap, (-value, value))
        if n < 0 < k:
            idx, v = heapq.heappop(heap)
            n += v
            k -= 1
        if n < 0 and k == 0:
            return rnd

    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
