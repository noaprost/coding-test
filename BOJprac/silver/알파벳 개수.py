import sys

s = sys.stdin.readline().rstrip()
count = [0 for _ in range(26)]

for ss in s:
    count[ord(ss) % 97] += 1

print(*count)
