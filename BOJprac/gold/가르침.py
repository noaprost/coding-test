# 1062
import sys

n, k = map(int, sys.stdin.readline().split())

if k < 5:
    exit(print(0))
elif k == 26:
    exit(print(n))

ans = 0
words = []
for _ in range(n):
    words.append(set(sys.stdin.readline().rstrip()))
alpha = [False for _ in range(26)]

for a in ["a", "n", "t", "i", "c"]:
    alpha[ord(a) - ord("a")] = True


def dfs(i, c):
    global ans

    if c == k - 5:
        count = 0
        for word in words:
            isLearn = True
            for w in word:
                if not alpha[ord(w) - ord("a")]:
                    isLearn = False
                    break
            if isLearn:
                count += 1
        ans = max(ans, count)
        return

    for j in range(i, 26):
        if not alpha[j]:
            alpha[j] = True
            dfs(j, c + 1)
            alpha[j] = False


dfs(0, 0)
print(ans)

# 비트마스킹
# import sys
# from itertools import combinations

# n, k = map(int, sys.stdin.readline().split())

# if k < 5:
#     exit(print(0))
# elif k == 26:
#     exit(print(n))


# def wordToBit(word):
#     bit = 0
#     for w in word:
#         bit = bit | (1 << ord(w) - ord("a"))
#     return bit


# words = [sys.stdin.readline().rstrip() for _ in range(n)]
# bits = list(map(wordToBit, words))
# base_bit = wordToBit("antic")

# words = [1 << i for i in range(26) if not (base_bit & 1 << i)]
# ans = 0
# for combination in combinations(words, k - 5):
#     count = 0
#     learn_bit = sum(combination) | base_bit
#     for bit in bits:
#         if bit & learn_bit == bit:
#             count += 1
#     ans = max(ans, count)
# print(ans)