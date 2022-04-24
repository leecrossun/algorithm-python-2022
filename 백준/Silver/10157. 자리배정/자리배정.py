# 자리배정
C, R = map(int, input().split()) # 공연장 크기
K = int(input()) # 대기번호
hall = list([False] * C for _ in range(R)) # 예매현황

x, y = 0, 0 # 현재 좌석
move = 0 # 방향
mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]

ans_x, ans_y = -1, -1
waiting = 1 # 대기번호
if C * R < K:
    print("0")
else:
    while 1:
        if waiting == K:
            ans_x, ans_y = x + 1, y + 1
            break
        hall[y][x] = True
        
        # 회전
        while 1:
            mv_y = y + my[move]
            mv_x = x + mx[move]
            if mv_x >= C or mv_x < 0 or mv_y >= R or mv_y < 0 or hall[mv_y][mv_x] == True:
                move = (move + 1) % 4
            else: break

        # 다음 좌석
        x, y = mv_x, mv_y
        waiting += 1

if ans_x != -1 and ans_y != -1:
    print(ans_x, ans_y)