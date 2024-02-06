n = int(input())
a = list(map(int, input().split()))

sorted_set_a = sorted(list(set(a)))

cnt_dict = {}

for idx, value in enumerate(sorted_set_a):
    cnt_dict[value] = idx

answer = []
for value in a:
    answer.append(cnt_dict[value])

print(*answer)