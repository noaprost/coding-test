# 1339
import sys

n = int(sys.stdin.readline())

# 알파벳마다 점수를 매기고 높은 값부터 큰 수를 할당해줌
# 그러면서도 앞에나온 애는 추가 점수를 받아야함

# A의 아스키코드는 65


tmp = ""

for _ in range(n):
    s1 = sys.stdin.readline().rstrip()
    tmp += s1
    tmp += "+"

i = 0
num = 9
while i < (len(tmp) - n):
    pass


s = list(map(int, tmp.split("+")[:n]))

print(sum(s))
