# Welcome to SMUPC!
import sys

n = int(sys.stdin.readline())
s = "WelcomeToSMUPC"
print(s[(n - 1) % 14])
