x, y, w, h = map(int, input().split())
print(min(min(x, abs(x - w)), min(y, abs(y - h))))
