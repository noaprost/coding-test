import sys

n = int(sys.stdin.readline())
co = set()

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        co.add(name)
    elif log == "leave":
        co.remove(name)

co = list(co)
co.sort(reverse=True)

for na in co:
    print(na)
