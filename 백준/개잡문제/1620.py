import sys

pokemon_dict = dict()

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in range(n):
    name = sys.stdin.readline().rstrip()
    pokemon_dict[name] = str(i + 1)
    pokemon_dict[str(i + 1)] = name

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    print(pokemon_dict[name])
