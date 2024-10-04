import math
from functools import reduce

n, s = map(int, input().split())
person_list = list(map(lambda x: abs(int(x) - s), input().split()))

answer = reduce(math.gcd, person_list)

print(answer)
