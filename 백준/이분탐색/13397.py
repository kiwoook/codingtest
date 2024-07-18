n, m = map(int, input().split())
arr = list(map(int, input().split()))


def divide(v):
    cnt = 1
    max_arr = arr[0]
    min_arr = arr[0]

    for a in arr:
        max_arr = max(max_arr, a)
        min_arr = min(min_arr, a)

        if max_arr - min_arr > v:
            cnt += 1
            max_arr = a
            min_arr = a
            if cnt > m:
                return False

    return True


answer = 0
start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    if divide(mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)
