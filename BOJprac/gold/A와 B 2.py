# 12919
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

def find(t):
    if len(t)==len(s):
        return t==s
    if t[0] == 'B' and find(t[:0:-1]):
        return True
    if t[-1] == 'A' and find(t[:-1]): 
        return True
    
if find(t):
    print(1)
else:
    print(0)
