import sys

order = {char: idx for idx, char in enumerate(
    "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
)}


def cnt_zero(s: str):
    return s.count('0')


def separate_str_num(s: str):
    str_list = []
    is_digit = False
    tmp = ''
    for char in s:
        if char.isdigit():
            if not is_digit:
                if tmp:
                    str_list.append(tmp)
                tmp = char
                is_digit = True
            else:
                tmp += char
        else:
            if is_digit:
                str_list.append(tmp)
                tmp = char
                is_digit = False
            tmp += char
    if tmp:
        str_list.append(tmp)
    return str_list


def sort_key(s: str):
    parts = separate_str_num(s)
    key = []
    for part in parts:
        if part.isdigit():
            key.append((0, int(part), cnt_zero(part)))
        else:
            key.append((1, [order[c] for c in part]))
    return key


n = int(sys.stdin.readline().rstrip())
file_list = [sys.stdin.readline().rstrip() for _ in range(n)]

file_list.sort(key=sort_key)

for file_name in file_list:
    print(file_name)
