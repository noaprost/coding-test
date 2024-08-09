# 1517
import sys


def merge_sort(start, end):
    global ans, nums

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        tmp = []
        x, y = start, mid + 1

        while x <= mid and y <= end:
            if nums[x] <= nums[y]:
                tmp.append(nums[x])
                x += 1
            else:
                tmp.append(nums[y])
                y += 1
                ans += (mid - x) + 1

        if x <= mid:
            tmp = tmp + nums[x : mid + 1]

        if y <= end:
            tmp = tmp + nums[y : end + 1]

        for i in range(len(tmp)):
            nums[start + i] = tmp[i]


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ans = 0

merge_sort(0, n - 1)
print(ans)
