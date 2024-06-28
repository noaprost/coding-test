# 1747
import sys

N = 1003001
a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if a[i]:
        primes.append(str(i))
        for j in range(2 * i, N + 1, i):
            a[j] = False


def isPalindrome(num):
    for left in range(len(num) // 2):
        right = len(num) - left - 1
        if num[left] != num[right]:
            return False

    return True


n = int(sys.stdin.readline())
for p in primes:
    if int(p) >= n and isPalindrome(p):
        exit(print(p))
