import sys


def put_dict(value):
    global note_dict
    value = int(value)
    note_dict[value] = 1


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    note_dict = dict()
    n = int(sys.stdin.readline().rstrip())
    note1 = list(map(put_dict, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split()))

    for v in note2:
        if note_dict.get(v) is not None:
            print("1")
        else:
            print("0")
