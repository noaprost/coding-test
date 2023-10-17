# DNA
# 해밍디스턴스의 합을 가장 작게 만드는 DNA를 찾는것이 목표
import sys

n, len = map(int, sys.stdin.readline().split())

dna = []

diff = [0] * n

for _ in range(n):
    d = sys.stdin.readline().strip()

    dna.append(d)
