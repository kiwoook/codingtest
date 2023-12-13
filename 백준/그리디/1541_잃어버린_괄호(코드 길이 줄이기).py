expression = input()
exp_list = expression.split('-')

for idx, exp in enumerate(exp_list):
    if '+' in exp:
        exp_list[idx] = sum(list(map(int, exp.split('+'))))
    else:
        exp_list[idx] = int(exp)

answer = exp_list[0]

for exp in exp_list[1:]:
    answer -= exp

print(answer)
