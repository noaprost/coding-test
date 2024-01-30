# idea : 유클리드 알고리즘
import sys

sys.set_int_max_str_digits(10000)


# 유클리드 알고리즘
def euclid(a, b):
    rm = a % b
    if rm == 0:
        return b

    while True:
        if b % rm == 0:
            return rm
        else:
            tmp = b % rm
            b = rm
            rm = tmp


# 숫자 입력
c1 = input()
n1 = input().split()
c2 = input()
n2 = input().split()

# 나눠져있는 숫자 곱하기
a = 1
b = 1

for n in n1:
    a = a * int(n)

for n in n2:
    b = b * int(n)

answer = euclid(a, b)
if answer > 999999999:  # 9자리 이상일 경우
    answer = answer % 1000000000
    print("{0:09d}".format(answer))
else:
    print(answer)
