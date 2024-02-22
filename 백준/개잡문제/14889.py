from itertools import combinations

score = []
min_value = int(1e9)
n = int(input())

for _ in range(n):
    score.append(list(map(int, input().split())))

a = {x for x in range(1, n)}

comb_a = set(list(combinations(a, 1)))

for comb1 in comb_a:
    set_comb1 = set(comb1)
    comb_b = set(list(combinations(a ^ set_comb1, 2)))
    comb1 = int(str(comb1)[1])
    for comb2 in comb_b:
        b1, b2 = comb2
        print(0, comb1, b1, b2 )
        min_value = min(min_value, abs(score[0][comb1] + score[comb1][0] - (score[b1][b2] + score[b2][b1])))


print(min_value)