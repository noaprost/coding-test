import sys


def create(n, idx, s):
    if idx == n:
        tmp = eval(s.replace(" ", ""))
        if tmp == 0:
            ans.append(s)
        return
    else:
        i = idx + 1
        create(n, i, s + " " + str(i))
        create(n, i, s + "+" + str(i))
        create(n, i, s + "-" + str(i))


caseNum = int(sys.stdin.readline())
for _ in range(caseNum):
    n = int(sys.stdin.readline())
    ans = []
    create(n, 1, "1")
    for a in ans:
        print(a)
    print()
