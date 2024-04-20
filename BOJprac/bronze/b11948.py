# 과목 선택
import sys

sScore = [int(sys.stdin.readline()) for _ in range(4)]
hScore = [int(sys.stdin.readline()) for _ in range(2)]

sScore.remove(min(sScore))

print(sum(sScore) + max(hScore))
