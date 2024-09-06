# 1439
import sys

s = list(sys.stdin.readline().rstrip())
toggle = s[0]
count = [0, 0]
count[int(s[0])] += 1

for i in range(1, len(s)):
    if s[i] == toggle:
        continue

    toggle = s[i]
    count[int(s[i])] += 1

print(min(count))
