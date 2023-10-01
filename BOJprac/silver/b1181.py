import sys

n = int(sys.stdin.readline())

word = [sys.stdin.readline().strip() for _ in range(n)]

word_set = set(word)

word_set = list(word_set)
word_set.sort()
word_set.sort(key=len)

for w in word_set:
    print(w)
