import sys

s = sys.stdin.readline().strip()

s = s.upper()
count = []
alpha = []

sList = list(s)

s1 = set(sList)

for ss in s1:
    count.append(sList.count(ss))
    alpha.append(ss)

if count.count(max(count)) != 1:
    print("?")
else:
    print(alpha[count.index(max(count))])
