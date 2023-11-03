# 통계학
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(n)]
count = [0] * (8002)
mode = []

# 산술평균
print(round(sum(nums) / n))

# 중앙값
nums.sort()
print(nums[int(n / 2)])

# 최빈값 : 여러개일때는 두번째로 작은 값 출력
for num in nums:
    count[num] += 1
m = max(count)
for num in nums:
    if count[num] == m:
        mode.append(num)
mode = set(mode)
mode = list(mode)
mode.sort()
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])

# 범위
print(max(nums) - min(nums))
