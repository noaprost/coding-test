# index 함수는 찾는 값이 없으면 예외를 발생 시킴 -> 문자열, 리스트, 튜플 사용 가능, 딕셔너리는 x
# <해결방법> i = somelist.index(x) if x in somelist else None
# find 함수는 없는 경우 -1을 리턴 -> 단, 문자열에서만 사용 가능, 리스트, 튜플 딕셔너리는 x
import sys

s = sys.stdin.readline().strip()

ans = [0 for _ in range(26)]

for a in range(97, 123):
    ans[a - 97] = s.find(chr(a))

for v in ans:
    print(v, end=" ")
