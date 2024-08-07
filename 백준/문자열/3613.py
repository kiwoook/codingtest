def checkCode(value: str):
    if value[0] == '_' or value[-1] == '_' or '__' in value or value[0].isupper():
        return 0

    flag = 0
    if '_' in value:
        for c in value:
            if c.isupper():
                flag = 1
                break
        if flag == 0:
            return 2

    elif value[0].islower() and ' ' not in value:
        return 1

    return 0


s = input()

answer = []

flag = checkCode(s)
if flag == 1:
    answer.append(s[0])

    for char in s[1:]:
        if char.isupper():
            answer.append('_')
            answer.append(char.lower())
        else:
            answer.append(char)
elif flag == 2:
    sw = 0
    for char in s:
        if char == '_':
            sw = 1
            continue
        elif sw == 1:
            answer.append(char.upper())
            sw = 0
        else:
            answer.append(char)
else:
    print("Error!")
    exit(0)

print(''.join(answer))
