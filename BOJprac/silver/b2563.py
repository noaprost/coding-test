import sys

n = int(sys.stdin.readline())

paper = [["x" for _ in range(100)] for _ in range(100)]


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            if paper[b + i][a + j] == "x":
                paper[b + i][a + j] = "o"

count = 0

for p in paper:
    count += p.count("o")

print(count)
