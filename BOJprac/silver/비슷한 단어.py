import sys

n = int(sys.stdin.readline())

ch = sys.stdin.readline().rstrip()
similer = 0
for _ in range(n - 1):
    com = list(ch)
    test = sys.stdin.readline().rstrip()
    count = 0

    for t in test:
        if t in com:
            com.remove(t)
        else:
            count += 1
    if count < 2 and len(com) < 2:
        similer += 1

print(similer)
