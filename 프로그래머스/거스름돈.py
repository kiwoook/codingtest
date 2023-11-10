def find_comb(money, n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]

    return dp[n]


def solution(n, money):  # n보다 큰 화폐는 치운다.
    able_money = []
    for m in money:
        if n >= m:
            able_money.append(m)

    if len(able_money) == 0:
        return 0

    return find_comb(money, n) % 1000000007


print(solution(5, [1, 2, 5]))
