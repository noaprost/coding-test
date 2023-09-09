import sys

n = int(sys.stdin.readline())

for _ in range(n):
    n, s = sys.stdin.readline().split()
    n = int(n)

    ans = ""

    for ss in s:
        ans += ss * n
    print(ans)
