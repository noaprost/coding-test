# 12^6 = 2,985,984


# 로또 번호 출력 함수
def lottoPrint(c, num):
    for i1 in range(c):
        for i2 in range(1, c + 1):
            for i3 in range(2, c + 2):
                for i4 in range(3, c + 3):
                    for i5 in range(4, c + 4):
                        for i6 in range(5, c + 5):
                            if i1 < i2 and i2 < i3 and i3 < i4 and i4 < i5 and i5 < i6:
                                print(
                                    num[i1],
                                    num[i2],
                                    num[i3],
                                    num[i4],
                                    num[i5],
                                    num[i6],
                                    end=" ",
                                )
    print("\n")


s = []
while True:  # 입력 전체를 하나의 리스트에 저장
    ip = input().split()
    if int(ip[0]) != 0:
        s.append(ip)
    else:
        break
# 테스트 케이스를 하나씩 꺼내서 진행
for ss in s:
    n = int(ss[0])
    c = n - 5
    num = ss[1:]
    lottoPrint(c, num)
