expression = input()

number_list = []
arithmetic_list = []

string_number = ""
for e in expression:
    if e == '+' or e == '-':
        arithmetic_list.append(e)
        number_list.append(int(string_number))
        string_number = ""
    else:
        string_number += e

number_list.append(int(string_number))
calcu_list = [0 for _ in range(len(number_list))]

i = 0
while "+" in arithmetic_list:
    if arithmetic_list[i] == '+':
        number_list[i] += number_list[i + 1]
        number_list.pop(i + 1)
        arithmetic_list.pop(i)
        i = -1
    i += 1

i = 0
while "-" in arithmetic_list:
    if arithmetic_list[i] == '-':
        number_list[i] -= number_list[i + 1]
        number_list.pop(i + 1)
        arithmetic_list.pop(i)
        i = -1
    i += 1

print(number_list[0])
