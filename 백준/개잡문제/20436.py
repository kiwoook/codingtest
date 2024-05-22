keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
pos_dict = dict()
answer = 0
for y, key in enumerate(keyboard):
    for x, k in enumerate(key):
        pos_dict[k] = (y, x)

left_finger, right_finger = input().split()
string = input()

for s in string:
    target_y, target_x = pos_dict[s]
    left_y, left_x = pos_dict[left_finger]
    right_y, right_x = pos_dict[right_finger]

    if s in 'qwertasdfgzxcv':
        answer += abs(target_x - left_x) + abs(target_y - left_y)
        left_finger = s
    else:
        answer += abs(target_x - right_x) + abs(target_y - right_y)
        right_finger = s
print(answer + len(string))
