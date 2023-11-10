def balance(s):
    chk = 0
    for idx, sin in enumerate(s):
        if sin == '(':
            chk += 1
        elif sin == ')':
            chk -= 1
        if chk == 0:
            return idx
    return len(s)


def correct(s):
    chk = 0
    for idx, sin in enumerate(s):
        if sin == '(':
            chk += 1
        elif sin == ')':
            chk -= 1
        if chk < 0:
            return False
    if chk == 0:
        return True


def reverse(u):
    a = ''
    for uin in u:
        if uin == '(':
            a += ')'
        if uin == ')':
            a += '('
    return a


def procedure(w):
    len_w = len(w)
    if len_w == 0:
        return ''
    idx = balance(w)
    u, v = w[0:idx + 1], w[idx + 1::]

    if correct(u):
        return u + procedure(v)
    else:
        return '(' + procedure(v) + ')' + reverse(u[1:-1])


def solution(p):
    return procedure(p)


print(solution("()))((()"))
