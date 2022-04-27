# 쇠막대기
from collections import deque
bracket = input()
stack = deque([])
stick, broken, remain = 0, 0, 0
temp = bracket[0]
for b in bracket:
    if b == "(":
        stack.append("(")
    elif b == ")":
        stack.pop()
        if temp == "(":
            stick += len(stack) + broken
            broken, remain = 0, len(stack)
        elif temp == ")":
            broken += 1
    temp = b

stick += remain
print(stick)