def solution(diffs, times, limit):

    left, right = 1, max(diffs)

    #  제한보다 낮으면 왼쪽으로 옮긴다.
    #  제한보다 높으면 오른쪽으로 옮긴다.
    # 첫번째는 안틀림
    while left < right:
        print(left, right)
        mid = (left + right) // 2
        total_time = 0

        for i in range(len(times)):
            if diffs[i] < mid:
                total_time += times[i]
            else:
                incorrect = diffs[i] - mid
                total_time += (times[i] + times[i - 1]) * incorrect + times[i]

        if total_time <= limit:
            right = mid
        else:
            left = mid + 1

    return left


print(solution([1, 5, 3], [2, 4, 7], 30))
