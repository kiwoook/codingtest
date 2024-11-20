a = input()
ops = input()
b = input()

a_zero_cnt = a.count('0')
b_zero_cnt = b.count('0')

if ops == "*":
    print('1' + '0' * (a_zero_cnt + b_zero_cnt))
else:
    diff = abs(a_zero_cnt - b_zero_cnt)
    max_value = list(max(a,b, key=lambda x: len(x)))
    max_value[diff] = str(int(max_value[diff]) + 1)
    print(''.join(max_value))
