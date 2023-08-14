# 하노이 탑 이동 순서


# start에서 end를 거쳐 n개의 원반을 이동하는 함수
def hanoi(n, start, end, via):
    if n == 1:
        move.append([start, end])
    else:
        hanoi(n - 1, start, via, end)
        move.append([start, end])
        hanoi(n - 1, via, end, start)


n = int(input())
move = []
hanoi(n, 1, 3, 2)

print(len(move))  # 이동 횟수
for m in move:
    print(m[0], m[1])  # 이동 순서
