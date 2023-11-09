import sys

n, m = map(int, sys.stdin.readline().split())

student = list(map(int, sys.stdin.readline().split()))

gaji = 0

gauge = 0

for s in student:
    if (gauge + s) < m:
        gauge += s
    else:
        gauge -= s
        gaji += 1

print(gaji)
