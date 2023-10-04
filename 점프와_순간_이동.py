def solution(n):
    ans = 0
    k = n

    while k != 0:
        if k % 2 == 0:
            k //= 2
        else:
            k -= 1
            ans += 1

    return ans


print(solution(5000))
