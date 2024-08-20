# 30982
# 두 개의 배낭 문제
# 다이나믹 프로그래밍
import sys

n, m, t = map(int, sys.stdin.readline().split())
q = list(map(int, sys.stdin.readline().split()))
p = int(sys.stdin.readline()) - 1

left_knapsack = [0 for _ in range(101)]
right_knapsack = [0 for _ in range(101)]
