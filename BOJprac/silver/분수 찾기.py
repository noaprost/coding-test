import sys

n = int(sys.stdin.readline())

sum = 0
i = 1

while n > sum:
    sum = int(i * (i + 1) / 2)
    i += 1

diff = sum - n

if i % 2 != 0:
    print("{0}/{1}".format(i - diff - 1, diff + 1))
else:
    print("{0}/{1}".format(diff + 1, i - diff - 1))
