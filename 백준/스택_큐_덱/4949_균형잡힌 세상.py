import sys

while 1:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    stack = []
    sw = 0
    for s in string:

        if s == '(':
            stack.append('(')
        if s == '[':
            stack.append('[')
        if s == ')':
            if len(stack) == 0 or stack.pop() != '(':
                sw = 1
                break
        if s == ']':
            if len(stack) == 0 or stack.pop() != '[':
                sw = 1
                break

    if sw == 1 or len(stack) > 0:
        print("no")
    else:
        print("yes")
