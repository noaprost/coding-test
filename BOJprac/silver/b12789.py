import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

stack = []

k = 1

for i in range(len(nums)):
    while stack and stack[-1] < nums[i]:
        tmp = stack.pop()
        if k != tmp:
            exit(print("Sad"))
        k += 1
    stack.append(nums[i])

while stack:
    tmp = stack.pop()
    if k != tmp:
        exit(print("Sad"))
    k += 1
print("Nice")
