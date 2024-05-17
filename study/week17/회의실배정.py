import sys

n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append([a, b])

meeting.sort(key=lambda x: (x[1], x[0]))

count = 1
endTime = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= endTime:
        count += 1
        endTime = meeting[i][1]

print(count)
