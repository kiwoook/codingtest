def solution(k, score):
    answer = []
    arr = []

    for s in score:
        arr.append(s)
        arr.sort(reverse=True)
        if len(arr) <= k:
            answer.append(arr[-1])
        else:
            answer.append(arr[k-1])
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
