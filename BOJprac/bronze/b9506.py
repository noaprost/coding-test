# 자기 자신의 절반까지만 약수를 구하는 것은
# 절반보다 큰수에 어떤걸 곱해도 자기 자신을 만들 수 없기 때문

import sys

n = int(sys.stdin.readline())
m = []
sum = 0

while n != -1:
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            m.append(i)
            sum += i
    if sum == n:
        print(n, "= ", end="")
        for i in range(len(m) - 1):
            print(m[i], "+ ", end="")
        print(m[len(m) - 1])
    else:
        print(n, "is NOT perfect.")

    n = int(sys.stdin.readline())
    m = []
    sum = 0
