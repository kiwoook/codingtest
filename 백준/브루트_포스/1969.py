import sys

molecule_list = ['A', 'C', 'G', 'T']
molecule_dict = {'A': 0, 'C': 1, "G": 2, "T": 3}

n, m = map(int, sys.stdin.readline().rstrip().split())
dna_list = []

for _ in range(n):
    dna_list.append(sys.stdin.readline().rstrip())

total = 0
answer = ''
for i in range(m):
    max_cnt = 0
    cnt_list = [0] * 4
    for k in range(n):
        cnt_list[molecule_dict[dna_list[k][i]]] += 1
        max_cnt = max(max_cnt, cnt_list[molecule_dict[dna_list[k][i]]])
    for k in range(4):
        if cnt_list[k] == max_cnt:
            answer += molecule_list[k]
            break
    total += n - max_cnt

print(answer)
print(total)
