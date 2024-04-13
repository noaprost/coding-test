import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

m = int(sys.stdin.readline())

findNum = list(map(int, sys.stdin.readline().split()))


# '정렬된 리스트'에서 `값이 특정 범위에 속하는 원소의 개수`를 구할 때 좋다.
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index


for f in findNum:
    print(count_by_range(num, f, f), end=" ")
