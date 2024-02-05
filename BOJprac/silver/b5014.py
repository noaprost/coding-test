# 스타트링크
# 주어진 조건에 맞게 층을 방문하다가 도착하지도 못했는데 모든 층에 방문했다면 갈 수 없음 표시
# 중간에 도착하면 바로 출력
import sys
from queue import Queue

totalFloor, start, end, up, down = map(int, sys.stdin.readline().split())
count = 0

building = [i for i in range(totalFloor + 1)]
que = Queue()

if start == end:
    exit(print(0))
