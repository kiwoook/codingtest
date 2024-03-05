import sys

a = set()
m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    commands = sys.stdin.readline().rstrip().split()

    if len(commands) == 1:
        if commands[0] == 'all':
            a = set([i for i in range(1, 21)])
        if commands[0] == 'empty':
            a = set()
    else:
        command, x = commands
        x = int(x)
        if command == 'add':
            a.add(x)
        if command == 'remove':
            if x in a:
                a.remove(x)
        if command == 'check':
            if x in a:
                print("1")
            else:
                print("0")
        if command == 'toggle':
            if x in a:
                a.remove(x)
            else:
                a.add(x)
