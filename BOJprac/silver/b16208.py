# 귀찮음

import sys

n = int(sys.stdin.readline())

stick = list(map(int, sys.stdin.readline().split()))

stick.sort()

total = 0


def cut(idx, len):
    global total
    # print(idx, len, total)
    if len == 1:
        return
    else:
        if len % 2 == 0:
            total += sum(stick[idx : (len // 2) + idx]) * sum(
                stick[(len // 2 + idx) : (len // 2 + idx) + (len // 2)]
            )
            cut(idx, (len // 2))
            cut((len // 2 + idx), (len // 2))
        else:
            total += sum(stick[idx : ((len + 1) // 2) + idx]) * sum(
                stick[
                    ((len + 1) // 2 + idx) : ((len - 1) // 2) + ((len + 1) // 2 + idx)
                ]
            )
            cut(idx, ((len + 1) // 2))
            cut(((len + 1) // 2 + idx), ((len - 1) // 2))


cut(0, sum(stick))

print(total)
