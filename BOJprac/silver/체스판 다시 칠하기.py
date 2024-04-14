import sys

n, m = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

result = []

for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    # 화이트로 시작
                    if board[x][y] != "B":
                        white += 1
                    # 블랙으로 시작
                    if board[x][y] != "W":
                        black += 1
                else:
                    if board[x][y] != "W":
                        white += 1
                    if board[x][y] != "B":
                        black += 1
        result.append(min(white, black))

print(min(result))
