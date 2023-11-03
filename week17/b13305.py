# 주유소
import sys

cityNum = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().split()))

oilPrice = list(map(int, sys.stdin.readline().split()))
minPrice = oilPrice[0]

money = 0

for i in range(cityNum - 1):
    if minPrice > oilPrice[i]:
        minPrice = oilPrice[i]
        money += road[i] * minPrice
    else:
        money += road[i] * minPrice

print(money)
