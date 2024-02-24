# 27989
import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [num[0]]  # 합



# dp에는 각 인덱스별 최대합을 저장하고
# 인덱스도 작고 값도 작은 애들 중에 가장 큰 dp값을 가지는 애를 가져와서 업데이트 -> 이걸 어떻게 하느냐

