
def is_string(args):
    args = str(args)
    return "숫자 :" + args

print(is_string(15))



a = 10
b = 20

tmp = a
a = b
b = tmp

print(a,b)

a = b = [0]

a[0] = 10

print(b)