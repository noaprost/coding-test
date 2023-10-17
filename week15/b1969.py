# DNA
# 해밍디스턴스의 합을 가장 작게 만드는 DNA를 찾는것이 목표
import sys

n, len = map(int, sys.stdin.readline().split())

dna = []

dnaBase = ["A", "C", "G", "T"]

ans = ""

diff = 0

for _ in range(n):
    d = sys.stdin.readline().strip()

    dna.append(d)

for i in range(len):
    dnaDiff = [0, 0, 0, 0]
    for j in range(n):
        dnaDiff[dnaBase.index(dna[j][i])] += 1
    ans += dnaBase[dnaDiff.index(max(dnaDiff))]
    diff += n - max(dnaDiff)

print(ans)
print(diff)
