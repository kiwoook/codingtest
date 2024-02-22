import sys


def calculate(tmp_list, multiple):
    # 괄호 연산
    cnt = 0
    for k in tmp_list:
        if k == '(' or k == '[':
            return -1
        cnt += k

    return multiple * cnt


expression = list(sys.stdin.readline().rstrip())
sw = 0
stack = []
try:
    for exp in expression:
        if exp == ')':
            tmp = []
            value = stack.pop()
            while value != '(':
                tmp.append(value)
                value = stack.pop()
            if len(tmp) == 0:
                stack.append(2)
            else:
                v = calculate(tmp, 2)
                if v == -1:
                    sw = 1
                    print("0")
                    break
                stack.append(v)
        elif exp == ']':
            tmp = []
            value = stack.pop()
            while value != '[':
                tmp.append(value)
                value = stack.pop()
            if len(tmp) == 0:
                stack.append(3)
            else:
                v = calculate(tmp, 3)
                if v == -1:
                    sw = 1
                    print("0")
                    break
                stack.append(v)
        else:
            stack.append(exp)
    if not sw:
        print(sum(stack))
except:
    print("0")
