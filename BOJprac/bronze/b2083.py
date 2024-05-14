import sys

name, tall, weight = sys.stdin.readline().split()

while name != "#":
    if int(tall) > 17:
        print(name, "Senior")
    elif int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")

    name, tall, weight = sys.stdin.readline().split()
