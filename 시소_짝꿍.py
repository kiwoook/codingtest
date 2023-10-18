def solution(weights):
    dp = [-1] * 4001
    same_cnt = [-1] * 1001

    cnt = 0
    for weight in weights:
        same_cnt[weight] += 1
        cnt += same_cnt[weight]
        same = same_cnt[weight]

        for multiple in range(2,5):
            value = weight * multiple
            dp[value] += 1
            cnt += dp[value] - same

    return cnt


print(solution([100, 100, 200, 300, 400]))
