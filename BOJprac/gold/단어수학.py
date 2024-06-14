# 1339
import sys

n = int(sys.stdin.readline())

words = []
dic = {}
s = set()

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    score = 1
    for i in range(len(word) - 1, -1, -1):
        if word[i] in dic:
            dic[word[i]] += score
        else:
            dic[word[i]] = score
        score *= 10
        s.add(word[i])

array = []
for item in s:
    array.append([dic[item], item])
array.sort(reverse=True)
max_value = 9

for item in array:
    dic[item[1]] = max_value
    max_value -= 1
sum = 0

for word in words:
    tmp = 0
    for i in range(len(word)):
        tmp += dic[word[i]]
        tmp *= 10
    tmp //= 10
    sum += tmp
print(sum)
