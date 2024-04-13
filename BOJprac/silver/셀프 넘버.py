n = 1

selfNum = [False + True for _ in range(11000)]

while n <= 10000:
    tmp = n
    for s in list(str(n)):
        tmp += int(s)
    selfNum[tmp] = False
    n += 1
    tmp = 0


for i in range(1, 10001):
    if selfNum[i]:
        print(i)
