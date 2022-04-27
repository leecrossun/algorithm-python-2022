# 괄호
# 쇠막대기
from collections import deque
N = int(input())
for _ in range(N):
    bracket = input()
    stack = deque([])
    isVPS = True
    for b in bracket:
        if b == "(":
            stack.append("(")
        elif b == ")":
            if len(stack) == 0:
                isVPS = False
            else:
                stack.pop()
    if isVPS and len(stack) == 0:
        print("YES")
    else:
        print("NO")