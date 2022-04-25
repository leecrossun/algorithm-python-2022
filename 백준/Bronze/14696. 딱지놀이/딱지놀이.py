# 딱지놀이
from collections import deque
N = int(input()) # 라운드 수
for _ in range(N):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    a.sort()
    b.sort()
    
    cnt = min(len(a), len(b))
    win = "D"
    for _ in range(cnt):
        a_score = a.pop()
        b_score = b.pop()

        if a_score > b_score:
            win = "A"
            break
        elif b_score > a_score:
            win = "B"
            break
    
    if win == "D":
        if len(a) > len(b):
            win = "A"
        elif len(a) < len(b):
            win = "B"

    print(win)