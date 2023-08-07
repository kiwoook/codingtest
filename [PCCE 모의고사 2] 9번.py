def solution(serial):
    answer = ''
    list_serial = list(serial)
    identify = []

    for i in range(0, len(serial), 2):
        identify.append(serial[i:i + 2])
    hap = 0
    for ser in list_serial:
        hap += int(ser)
    print(identify)
    print(list_serial)
    for idx, idt in enumerate(identify):
        s = ''
        if idx <= 1:
            if idt == '01':
                s += 'male'
            elif idt == '02':
                s += 'female'
            elif idt == '10':
                s += 'operation'
            elif idt == '11':
                s += 'sales'
            elif idt == '12':
                s += 'develop'
            elif idt == '13':
                s += 'finance'
            elif idt == '14':
                s += 'law'
            elif idt == '15':
                s += 'research'
            else:
                s += idt + 'team'
            s += '/'
        if idx == 2:
            s += str(int(idt)) + 'team' + '/'
        if idx == 3:
            if hap % 13 == int(idt):
                s += 'valid'
            else:
                s += 'invalid'
        answer += s

    return answer


[x,y] = [1,2]
print(not 0)

print(x,y)
