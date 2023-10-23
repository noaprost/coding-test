import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    fibonacci = [[1, 0], [0, 1]]
    num = int(sys.stdin.readline())

    i = 2
    while i <= num:
        fibonacci.append(
            [
                fibonacci[i - 1][0] + fibonacci[i - 2][0],
                fibonacci[i - 1][1] + fibonacci[i - 2][1],
            ]
        )
        i += 1

    print(fibonacci[num][0], fibonacci[num][1])
