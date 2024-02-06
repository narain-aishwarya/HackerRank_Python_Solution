# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
d = deque()
for i in range(n):
    commands, *args = input().split()
    operator = getattr(d,commands)
    operator(*args)
print(*d)

