# 25206
import sys

sum = 0.0
num = 0.0

for _ in range(20):
    s = list(sys.stdin.readline().split())

    if s[2] == "A+":
        sum += float(s[1]) * 4.5
        num += float(s[1])
    elif s[2] == "A0":
        sum += float(s[1]) * 4.0
        num += float(s[1])
    elif s[2] == "B+":
        sum += float(s[1]) * 3.5
        num += float(s[1])
    elif s[2] == "B0":
        sum += float(s[1]) * 3.0
        num += float(s[1])
    elif s[2] == "C+":
        sum += float(s[1]) * 2.5
        num += float(s[1])
    elif s[2] == "C0":
        sum += float(s[1]) * 2.0
        num += float(s[1])
    elif s[2] == "D+":
        sum += float(s[1]) * 1.5
        num += float(s[1])
    elif s[2] == "D0":
        sum += float(s[1]) * 1.0
        num += float(s[1])
    elif s[2] == "F":
        sum += float(s[1]) * 0.0
        num += float(s[1])
    elif s[2] == "P":
        continue

print(sum / num)
