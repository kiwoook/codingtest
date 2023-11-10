def solution(arr, query):
    for idx, q in enumerate(query):
        if idx % 2 == 0:
            arr = arr[0:q+1]
        else:
            arr = arr[q::]
    return arr

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))