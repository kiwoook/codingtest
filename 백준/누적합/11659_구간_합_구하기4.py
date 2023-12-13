# 구간 합문제는 a~b의 구간합에 대해서는
# b까지의 누적합에서 a-1까지의 누적합을 뺴서 구현한다.

def prefixSum(start, end):
    if start == 0:
        return pnum[end]

    return pnum[end] - pnum[start-1]


n, m = map(int, input().split())
number_list = list(map(int, input().split()))

pnum = [0 for _ in range(n)]
pnum[0] = number_list[0]

for i in range(1, n):
    pnum[i] = pnum[i - 1] + number_list[i]

for i in range(m):
    s, e = map(int, input().split())
    print(prefixSum(s-1, e-1))
