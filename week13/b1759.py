# 암호 만들기

import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
crypto = list(sys.stdin.readline().strip().split(" "))
crypto.sort()
con = 0  # 자음 개수
vow = 0  # 모음 개수

if __name__ == "__main__":
    for com in combinations(crypto, l):
        for c in com:
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                vow += 1
            else:
                con += 1
        if vow >= 1 and con >= 2:
            print("".join(com))

        con = 0
        vow = 0
