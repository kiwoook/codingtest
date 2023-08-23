# 괄호를 회전시킨다.
# 올바른 괄호인지 확인한다.
# 포개진 경우는 어떻게 해야할까?

def check(s):
    stack = []
    open_w = ['{', '(', '[']
    close_w = ['}', ')', ']']
    for al in s:
        if al == '[' or al == '(' or al == '{':
            stack.append(al)
        if al == ']' or al == ')' or al == '}':
            if stack:
                if close_w.index(al) != open_w.index(stack.pop()):
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    s_list = list(s)
    for x in range(len(s)):
        s_list.append(s_list.pop(0))
        if check(''.join(s_list)):
            answer += 1
    return answer


print(solution("}]()[{"))
