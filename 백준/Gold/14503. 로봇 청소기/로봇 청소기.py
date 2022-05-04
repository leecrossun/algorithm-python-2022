# 로봇 청소기
import copy
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)] # 1 벽 / 0 통로

is_clean = copy.deepcopy(room) # 1 청소 완료 / 0 청소 가능
# 북 동 남 서
mr = [-1, 0, 1, 0]
mc = [0, 1, 0, -1]

ans = 1
turn = 0
mv_r, mv_c, mv_d = r, c, d
is_clean[r][c] = 1
while 1:
    mv_d = (mv_d + 3) % 4 # 가상 회전
    turn += 1
    mv_r, mv_c = r + mr[mv_d], c + mc[mv_d]

    if is_clean[mv_r][mv_c] == 0:
        is_clean[mv_r][mv_c] = 1
        r, c, d = mv_r, mv_c, mv_d
        is_clean[r][c] = 1
        turn = 0
        ans += 1
    elif turn >= 4:
        back_d = (mv_d + 2) % 4
        back_r, back_c = r + mr[back_d], c + mc[back_d]
        if room[back_r][back_c] == 1:
            break
        else:
            r, c = back_r, back_c
            turn = 0
print(ans)