import sys

s = sys.stdin.readline().strip()
n = len(s)
c = False

for i in range(n):
    if s[i] == s[n - i - 1]:
        c = True
    else:
        c = False
        break

if c:
    print(1)
else:
    print(0)
