# 가장 긴 증가하는 부분 수열
# LIS (Longest Increasing Subsequence)
# 이진 탐색을 이용하면 dp만 사용했을 때에 비해 O(nlogn)의 짧은 시간 복잡도를 가지고
# 길이뿐만 아니라 수열이 어떤것인지도 구할 수 있다.
# dp의 경우 시간복잡도는 O(n^2)
from bisect import bisect_left
import sys

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
dp = [1]
x = [array[0]]

for i in range(1, len(array)):
    if array[i] > x[-1]:  # 현재 값이 x 배열의 마지막 값보다 클 경우
        x.append(array[i])  # x 배열에 현재 값을 추가해 주고
        dp.append(dp[-1] + 1)  # 증가 부분 수열의 길이를 1 증가시킨다.
    else:  # 그렇지 않을 경우
        idx = bisect_left(x, array[i])  # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
        x[idx] = array[i]  # x 배열의 idx 위치에 현재 값을 넣어준다.
print(dp[-1])
