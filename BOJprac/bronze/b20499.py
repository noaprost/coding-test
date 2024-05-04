# Darius님 한타 안 함?
import sys

k, d, a = map(int, sys.stdin.readline().split("/"))

if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")