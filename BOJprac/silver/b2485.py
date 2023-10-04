import sys


def euclid(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


# 가로수 사이 간격들이 담길 배열
dis = []

n = int(sys.stdin.readline())  # 가로수 개수

for i in range(n):
    a = int(sys.stdin.readline())

    if i > 0:
        dis.append(a - tmp)

    tmp = a

x = euclid(dis[0], dis[1])

for i in range(2, len(dis)):
    x = euclid(x, dis[i])

count = 0

for d in dis:
    count += d // x

print(count - len(dis))

# 여러 수의 최대 공약수를 뽑아야 하는디이
