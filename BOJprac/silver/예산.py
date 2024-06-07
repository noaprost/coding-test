import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
total = int(input())

start = 0
end = max(nums)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(n):
        if nums[i] >= mid:
            count += mid
        else:
            count += nums[i]

    if count <= total:
        start = mid + 1
    else:
        end = mid - 1

print(end)
