# 7453
import sys

n = int(sys.stdin.readline())

a_list, b_list, c_list, d_list = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

ab = []
for a in a_list:
    for b in b_list:
        ab.append(a + b)
ab.sort()

cd = []
for c in c_list:
    for d in d_list:
        cd.append(c + d)
cd.sort()

ans = 0
left, right = 0, len(cd) - 1
sum = 0

while 0 <= right and left < len(ab):
    sum = ab[left] + cd[right]
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        x = 1
        for i in range(left + 1, len(ab)):
            if ab[left] == ab[i]:
                x += 1
            else:
                break

        y = 1
        for i in range(right - 1, -1, -1):
            if cd[right] == cd[i]:
                y += 1
            else:
                break
            
        ans += x * y
        left += x
        right -= y

print(ans)
