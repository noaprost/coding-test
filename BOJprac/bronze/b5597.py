import sys

check = [0 for _ in range(30)]

for i in range(28):
    s = int(sys.stdin.readline())
    check[s - 1] = 1

for i in range(30):
    if check[i] == 0:
        print(i + 1)
