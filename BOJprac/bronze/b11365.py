# !밀비 급일
import sys

s = list(sys.stdin.readline().split())
while s != ["END"]:
    for i in range(len(s)):
        tmp = list(s[i])
        tmp.reverse()
        s[i] = "".join(tmp)

    s.reverse()
    print(" ".join(s))
    s = list(sys.stdin.readline().split())
