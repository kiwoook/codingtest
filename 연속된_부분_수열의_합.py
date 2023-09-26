def solution(sequence, k):
    left, right = 0, 0
    first, second = 0, 1000000
    total = sequence[0]

    while right < len(sequence):
        if total == k and second - first > right - left:
            first, second = left, right
            continue
        if total <= k:
            right += 1
            if right >= len(sequence):
                break
            total += sequence[right]
        if total > k:
            left += 1
            total -= sequence[left - 1]
        print(left, right, total)
    return [first, second]


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
