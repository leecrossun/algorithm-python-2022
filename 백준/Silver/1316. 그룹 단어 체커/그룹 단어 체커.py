# 그룹 단어 체커 - 구현
from collections import deque
N = int(input())
ans = 0
for _ in range(N):
    S = input()
    temp = deque([])
    is_group = True
    pre_word = ""
    for s in S:
        if s in temp and pre_word != s:
            is_group = False
            break
        elif s not in temp:
            temp.append(s)
        pre_word = s
    if is_group: ans += 1
print(ans)