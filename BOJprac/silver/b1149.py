# RGB 거리

import sys

homeNum = int(sys.stdin.readline())

rgbPrice = [list(map(int, sys.stdin.readline().split())) for _ in range(homeNum)]

price = [rgbPrice[0][0], rgbPrice[0][1], rgbPrice[0][2]]

for i in range(1, homeNum):
    price[0] += min(rgbPrice[i][1], rgbPrice[i][2])
    price[1] += min(rgbPrice[i][0], rgbPrice[i][2])
    price[2] += min(rgbPrice[i][0], rgbPrice[i][1])
    print(price)
