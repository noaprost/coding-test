# 팩토리얼 3
import sys

n = int(sys.stdin.readline())

facto = 1

for i in range(2, n + 1):
    facto *= i

print(facto)
