# 정보섬의 대중교통
import sys

moveTime, busAlive, subwayAlive = map(int, sys.stdin.readline().split())

if busAlive == subwayAlive:
    print("Anything")
elif busAlive < subwayAlive:
    print("Bus")
else:
    print("Subway")
