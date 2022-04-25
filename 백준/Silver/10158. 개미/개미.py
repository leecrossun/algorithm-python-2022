# 개미
w, h = map(int, input().split()) # 가로, 세로
x, y = map(int, input().split()) # 출발 좌표
t = int(input())

x_cnt = (x + t) % (2 * w)
y_cnt = (y + t) % (2 * h)

x_move = x_cnt if x_cnt <= w else w - (x_cnt - w)
y_move = y_cnt if y_cnt <= h else h - (y_cnt - h)

print(x_move, y_move)