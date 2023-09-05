# 선물
import sys
import math

n, l, w, h = map(int, sys.stdin.readline().split())

maxLen = min(l, w, h)
len = maxLen
minLen = 0

q1 = l // len
q2 = w // len
q3 = h // len

num = q1 * q2 * q3

while True:
    if n >= num:
        if round(len, 15) == round((minLen + len) / 2, 15):
            break
        len = round((minLen + len) / 2, 15)
        q1 = l // len
        q2 = w // len
        q3 = h // len

        num = q1 * q2 * q3

    elif n < num:
        if round(len, 15) == round((len + maxLen) / 2, 15):
            break
        len = round((len + maxLen) / 2, 15)
        q1 = l // len
        q2 = w // len
        q3 = h // len

        num = q1 * q2 * q3

print(len)
