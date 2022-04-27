# 에디터
from collections import deque
from sys import stdin
left = list(stdin.readline().strip())
N = int(input())
right = deque([])

for _ in range(N):
    cmd = stdin.readline().strip()
    if cmd == "L": # 커서를 왼쪽으로
        if left: right.append(left.pop())
    elif cmd == "D": # 커서를 오른쪽으로
        if right: left.append(right.pop())
    elif cmd == "B":
        if left: left.pop()
    else:
        c1, c2 = map(str, cmd.split())
        left.append(c2)
        
print(''.join(left), end='')
print(''.join(reversed(right)), end='')