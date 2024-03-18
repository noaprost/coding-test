# 세금
import sys

n = int(sys.stdin.readline())

print(n - int(n * 22 / 100), end=" ")
print(int(n * 80 / 100) + (int(n * 20 / 100) - int(int(n * 20 / 100) * 22 / 100)))
