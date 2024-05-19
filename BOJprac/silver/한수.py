import sys

n = int(sys.stdin.readline())

ans = 0

for i in range(1, n + 1):
    num = str(i)
    if len(num) == 1 or len(num) == 2:
        ans += 1
    else:
        diff = int(num[0]) - int(num[1])
        for j in range(1, len(num) - 1):
            if diff != int(num[j]) - int(num[j + 1]):
                break
        else:
            ans += 1
            
print(ans)
