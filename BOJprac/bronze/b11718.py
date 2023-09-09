import sys

i = 0
while i <= 100:
    try:
        s = sys.stdin.readline().strip()
        print(s)
    except:
        break

    i += 1
