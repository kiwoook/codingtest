import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

while a != 0 and b != 0 and c != 0:
    side_list = sorted([a, b, c])
    if not (side_list[0] + side_list[1] > side_list[2]):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

    a, b, c = map(int, sys.stdin.readline().rstrip().split())
