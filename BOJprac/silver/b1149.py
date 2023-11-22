# RGB 거리

import sys

homeNum = int(sys.stdin.readline())

rgbPrice = [list(map(int, sys.stdin.readline().split())) for _ in range(homeNum)]

price = [[rgbPrice[0][0], 1], [rgbPrice[0][1], 2], [rgbPrice[0][2], 3]]
