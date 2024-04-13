import sys

s = sys.stdin.readline().strip()
count = 0

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in cro:
    if c in s:
        count += s.count(c)

count += len(s) - count * 2

print(count)
