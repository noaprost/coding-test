import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    c = True
    check = []

    for i in range(len(s)):
        if s[i] in check:
            if s[i - 1] != s[i]:
                c = False
                break
        else:
            check.append(s[i])

    if c:
        count += 1

print(count)
