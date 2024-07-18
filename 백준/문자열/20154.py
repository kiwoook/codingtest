values = [
    3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1
]

# 알파벳 리스트
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# 알파벳을 값에 매핑
alpha_to_num = {alphabet[i]: values[i] for i in range(len(alphabet))}

answer_list = []

s = input()

for char in s:
    answer_list.append(alpha_to_num[char])

while len(answer_list) != 1:
    tmp = []
    for idx in range(0, len(answer_list), 2):
        if idx + 1 == len(answer_list):
            tmp.append(answer_list[idx])
        else:
            tmp.append((answer_list[idx] + answer_list[idx + 1]) % 10)
    answer_list = tmp

if answer_list[0] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
