# 31248
import sys


def move(tiles, s, e):
    if tiles == 0:
        return

    move(tiles - 1, s, 3 - s - e)
    print("ABC"[s], "ABC"[e])
    move(tiles - 1, 3 - s - e, e)


n = int(sys.stdin.readline())
dp = [0, 1]
for i in range(2, 21):
    dp.append(2 ** (i - 2) - 1 + 3 + dp[i - 2])
print(dp[n])

disk_pos = 0
while n >= 2:
    move(n - 2, disk_pos, 2 - disk_pos)
    print("ABC"[disk_pos], "B")
    print("ABC"[disk_pos], "D")
    print("B", "D")

    n -= 2
    disk_pos = 2 - disk_pos

if n == 1:
    print("ABC"[disk_pos], "D")
