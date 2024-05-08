# 메모리 초과

# import sys

# n = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(n)]

# count_dict = {}

# for num in arr:
#     if num in count_dict:
#         count_dict[num] += 1

#     else:
#         count_dict[num] = 1

# result = []

# for num in range(max(arr) + 1):
#     while num in count_dict and count_dict[num] != 0:
#         result.append(num)
#         count_dict[num] -= 1


# for r in result:
#     print(r)
