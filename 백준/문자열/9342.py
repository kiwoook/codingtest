import re
import sys


def is_valid_chromosome(s):
    # 정규 표현식 패턴
    pattern = r'^[ABCDEF]?[A]+[F]+[C]+[ABCDEF]?$'
    # 패턴과 입력 문자열이 매칭되는지 확인
    return bool(re.match(pattern, s))


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    s = sys.stdin.readline().rstrip()

    if is_valid_chromosome(s):
        print("Infected!")
    else:
        print("Good")
