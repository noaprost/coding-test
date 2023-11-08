# 회의실
# 데이터를 어떻게 저장할것인가
import sys

n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append([a, b])

meeting.sort(key=lambda x: x[1])
print(meeting)

maxTime = meeting[-1][0]
