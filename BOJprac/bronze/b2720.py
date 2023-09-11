import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r = int(sys.stdin.readline())
    q = r // 25
    d = (r % 25) // 10
    n = ((r % 25) % 10) // 5
    p = ((r % 25) % 10) % 5
    print(q, d, n, p)
