import sys

x = []
y = []

for _ in range(3):
    xx, yy = map(int, sys.stdin.readline().split())

    x.append(xx)
    y.append(yy)

if x[0] == x[1]:
    x1 = x[2]
else:
    if x[0] == x[2]:
        x1 = x[1]
    else:
        x1 = x[0]

if y[0] == y[1]:
    y1 = y[2]
else:
    if y[0] == y[2]:
        y1 = y[1]
    else:
        y1 = y[0]

print(x1, y1)
