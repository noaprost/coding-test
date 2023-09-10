import sys

a = []

for i in range(5):
    s = list(sys.stdin.readline().strip())
    for j in range(15 - len(s)):
        s.append(" ")
    a.append(s)

for i in range(15):
    for j in range(5):
        if a[j][i] != " ":
            print(a[j][i], end="")
