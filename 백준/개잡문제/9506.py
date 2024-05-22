import sys

n = int(sys.stdin.readline().rstrip())


def sum_div(num):
    result = []
    hap = 0
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
            hap += i

    result.sort()
    return sum(result), ' + '.join(map(str, result))


while n != -1:
    hap, answer = sum_div(n)

    if hap == n:
        print(str(n) + " = " + answer)
    else:
        print(str(n) + " is NOT perfect.")

    n = int(sys.stdin.readline().rstrip())
