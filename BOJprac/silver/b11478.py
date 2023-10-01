# 부분집합이지만 원소 하나하나가 아닌 순서까지 고려
import sys

arr = sys.stdin.readline().strip()
result = set()

for i in range(len(arr) + 1):
    for j in range(1, len(arr) + 1):
        result.add(arr[i:j])

print(len(result) - 1)  # 공집합 제거
