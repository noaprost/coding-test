import sys

n, m = map(int, sys.stdin.readline().split())

dogam_nums = {}

for i in range(n):
    dogam_nums[i + 1] = sys.stdin.readline().strip()

dogam_names = {v: k for k, v in dogam_nums.items()}

tmp = [sys.stdin.readline().strip() for _ in range(m)]

for t in tmp:
    try:
        if isinstance(int(t), int):
            print(dogam_nums[int(t)])
    except:
        print(dogam_names[t])
