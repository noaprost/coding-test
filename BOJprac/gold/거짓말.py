# 1043
import sys

n, m = map(int, sys.stdin.readline().split())

trueMan = [False] * (n+1)
trueParty = [False] * (m)

man = list(map(int, sys.stdin.readline().split()))[1:]

for tr in man:
    trueMan[tr] = True

party = []

flag = True

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))[1:]
    party.append(tmp)

# 진실 리스트 만들기
while flag:
    flag = False
    for i in range(m):
        if(not trueParty[i]):
            for t in party[i]:
                if(trueMan[t]):
                    for tt in party[i]:
                        trueMan[tt] = True
                    trueParty[i] = True
                    flag = True
                    break


print(trueParty.count(False))