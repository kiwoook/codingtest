def solution(s):
    s = list(' ' + s.lower())

    for i in range(0, len(s)-1):
        if s[i] == ' ' and s[i+1].isascii():
            s[i+1] = s[i+1].upper()
    return ' '.join(s[1:])


print(solution("Hell  yEa "))
