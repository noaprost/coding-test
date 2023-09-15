import sys

m = int(sys.stdin.readline())

n = int(sys.stdin.readline())

ans = []
isPrime = True
sum = 0

for i in range(m, n + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        ans.append(i)
        sum += i
    isPrime = True

if len(ans) == 0:
    print(-1)
else:
    print(sum)
    print(ans[0])
