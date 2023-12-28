import sys

money = 1000 - int(sys.stdin.readline())

count = 0

if money >= 500:
    count += money // 500
    money = money % 500

if money >= 100:
    count += money // 100
    money = money % 100

if money >= 50:
    count += money // 50
    money = money % 50

if money >= 10:
    count += money // 10
    money = money % 10

if money >= 5:
    count += money // 5
    money = money % 5

if money >= 1:
    count += money // 1
    money = money % 1

print(count)
