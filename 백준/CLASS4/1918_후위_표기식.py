expression = list(input())


# 1. 이미 존재하는 괄호들을 합치는 작업
# 2. *, / 만날 경우 앞뒤로 괄호를 만들고 처음부터 다시 작업
# 3. +, - 만날 경우 앞뒤로 괄호를 만들고 처음부터 다시 작업
# 4. 모든 문자열을 한개씩 분리시키고
# 4. 스택 구조 활용 (, )이용
# 5. 후위로 표기하고 괄호를 제거하면서 문자 자체를 합치기

def priority1(arr):
    i = 1
    while '*' in arr or '/' in arr:
        if arr[i] == '*' or arr[i] == '/':
            temp = '(' + arr[i - 1] + arr[i] + arr[i + 1] + ')'
            arr[i - 1:i + 2] = [temp]
            i = 0
        i += 1
    return arr


def priority2(arr):
    i = 1
    # 3번 작업 시행
    while '+' in arr or '-' in arr:
        if arr[i] == '+' or arr[i] == '-':
            temp = '(' + arr[i - 1] + arr[i] + arr[i + 1] + ')'
            arr[i - 1:i + 2] = [temp]
            i = 0
        i += 1
    return arr


# 1번 작업 시행
stack = []
for exp in expression:
    if exp == ')':
        tmp = []
        value = stack.pop()
        while value != '(':
            tmp.append(value)
            value = stack.pop()
        tmp.reverse()
        tmp = priority1(tmp)
        tmp = priority2(tmp)
        exp = '(' + ''.join(tmp) + ')'
    stack.append(exp)

# 3번작업시행
stack = priority1(stack)
# 4번작업시행
stack = priority2(stack)

expression = list(''.join(stack))

# 4번 이후 실행

stack = []
for exp in expression:
    if exp == ')':
        tmp = []
        value = stack.pop()
        operator = ''
        while value != '(':
            if value == '+' or value == '-' or operator == '/' or operator == '*':
                operator = value
            else:
                tmp.append(value)
            tmp.reverse()
            exp = ''.join(tmp) + operator
            value = stack.pop()
    stack.append(exp)

print(*stack)
