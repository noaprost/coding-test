# 5525
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())

i = 0
count = 0
flag = True

while i < m:
    if s[i] == "I":
        j = 0
        while j < n:
            if not i + 2 * j + 2 < m:
                exit(print(count))

            if s[i + 2 * j + 1] == "O" and s[i + 2 * j + 2] == "I":
                j += 1

            else:
                flag = False
                break

        i += 2 * j + 1

        while flag:
            count += 1

            if i + 1 < m:
                if s[i] == "O" and s[i + 1] == "I":
                    i += 2
                else:
                    flag = False
            else:
                flag = False
        flag = True
    else:
        i += 1

print(count)
