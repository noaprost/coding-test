from collections import Counter
import sys


def return_to_origin(n, k, text, destination):
    fx, fy = destination
    dist = abs(fx) + abs(fy)
    if dist == 0:
        return "YES"
    x, y = 0, 0
    for t in text[:-1]:  # 명령어 순회
        if t == "U":
            y += 1
        elif t == "D":
            y -= 1
        elif t == "L":
            x -= 1
        elif t == "R":
            x += 1
        dist_new = abs(x) + abs(y)
        if fx * y == fy * x and dist_new // dist < k and dist_new % dist == 0:
            return "YES"
    return "NO"


n, k = map(int, sys.stdin.readline().split())  # n: 명령어의 길이, k: 반복 횟수
text = sys.stdin.readline().rstrip()
counter = Counter(text)
ud = counter["U"] - counter["D"]
lr = counter["R"] - counter["L"]
destination = (lr, ud)

print(return_to_origin(n, k, text, destination))
