import sys

n = int(sys.stdin.readline())  # 입력 받을 개수
num = [int(sys.stdin.readline()) for i in range(int(n))]  # 입력 받은 수의 배열

mx = max(num)

eratos = [False, False] + [True for _ in range(2, mx + 1)]

for i in range(2, mx+1):
    if eratos[i]:
        for j in range(2 * i, mx + 1, i):
            eratos[j] = False

for n in num:
    count = 0
    for i in range((n // 2) + 1):
        if eratos[i] and eratos[n-i]:
            count += 1
    print(count)
