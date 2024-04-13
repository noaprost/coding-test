import sys

commandNum = int(sys.stdin.readline())

stack = []

for _ in range(commandNum):
    c = sys.stdin.readline().strip()
    if c[0] == "1":  # 정수를 스택에 넣음
        a, b = map(int, c.split())
        stack.append(b)
    else:
        c = int(c)

        if c == 2:  # 스택에 정수가 있다면 맨위 정수를 빼고 출력, 없다면 -1 출력
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)

        elif c == 3:  # 스택에 있는 정수 개수 출력
            print(len(stack))

        elif c == 4:  # 스택이 비어있으면 1, 아니면 0 출력
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        elif c == 5:  # 스택에 정수가 있다면 맨위 정수 출력, 없다면 -1 출력
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)

