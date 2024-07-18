# 메모리 초과


# 3651
# import sys
# import copy

# m = int(sys.stdin.readline())

# dp = [0, 1] + [0 for _ in range(m)]
# ans = []
# cnt = 0

# for n in range(1, m + 2):
#     tmp = copy.deepcopy(dp)
#     for k in range(1, m + 2):
#         v = tmp[k - 1] + tmp[k]
#         if k == 1:
#             dp[k] = 1
#         elif k != n:
#             dp[k] = v
#             if dp[k] == m:
#                 ans.append([n, k])
#                 cnt += 1
#         elif k == n:
#             dp[k] = 1
# print(cnt)
# for a in ans:
#     print(a[0] - 1, a[1] - 1)
