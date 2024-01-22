# 평균 점수
import sys

score = []
for _ in range(5):
    n = int(sys.stdin.readline())
    if n < 40:
        score.append(40)
    else:
        score.append(n)


s = sum(score)

print(s // 5)
