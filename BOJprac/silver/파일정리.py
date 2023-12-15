# 20291
import sys

n = int(sys.stdin.readline())
dict = {}
extension = set()

for _ in range(n):
    file = sys.stdin.readline().rstrip().split(".")
    if dict.get(file[1], -2) == -2:
        dict[file[1]] = 1
    else:
        dict[file[1]] += 1
    extension.add(file[1])

extension = list(extension)
extension.sort()

for ex in extension:
    print(ex, dict[ex])
