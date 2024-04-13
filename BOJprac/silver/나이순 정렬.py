import sys

n = int(sys.stdin.readline())

info = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    info.append([age, name])

info.sort(key=lambda x: int(x[0]))

for i in info:
    print(int(i[0]), i[1])
