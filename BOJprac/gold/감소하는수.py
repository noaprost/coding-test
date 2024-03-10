# 1038
import sys
from itertools import combinations

target = int(sys.stdin.readline())

dec = []

# 조합을 뒤집으면 항상 감소하는 수
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = "".join(list(map(str, reversed(list(j)))))
        dec.append(int(num))

dec.sort()
if target >= len(dec):
    print(-1)
else:
    print(dec[target])
