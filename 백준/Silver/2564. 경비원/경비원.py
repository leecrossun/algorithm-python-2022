# 경비원
w, h = map(int, input().split()) # 가로, 세로
n = int(input()) # 상점 개수
shops = list(list(map(int, input().split())) for _ in range(n)) # 상점
my_direction, my_dist = map(int, input().split()) # 현재 위치

# 위치 변환
def change_loc(direction):
    if direction == 2: # 남
        return 3
    elif direction == 3: # 서
        return 2
    else:
        return direction

# 거리 변환 (오른쪽기준으로)
def change_dist(direction, dist):
    if direction == 4: # 동
        return h - dist
    elif direction == 1: # 북
        return w - dist
    else:
        return dist

# 건너갈 때 가로, 세로 선택
def choose_len(direction):
    if direction == 1 or direction == 3:
        return w
    else:
        return h

my_direction = change_loc(my_direction)
my_dist = change_dist(my_direction, my_dist)

for i in range(len(shops)):
    shops[i][0] = change_loc(shops[i][0])
    shops[i][1] = change_dist(shops[i][0], shops[i][1])

# 거리 계산
total_dist = 0
for shop in shops:
    s_direction, s_dist = shop[0], shop[1]
    relate = s_direction - my_direction
    if relate == 1 or relate == -3: # 오른쪽 위
        total_dist += (choose_len(my_direction) - my_dist) + s_dist
    elif relate == -1 or relate == 3: # 왼쪽 위
        total_dist += my_dist + (choose_len(s_direction) - s_dist)
    elif relate == 0: # 같은편
        total_dist += abs(s_dist - my_dist)
    else: # 건너편
        cross = w if choose_len(my_direction) == h else h
        calc_left = my_dist + (choose_len(s_direction) - s_dist) + cross # 시계방향
        calc_right = choose_len(my_direction) - my_dist + s_dist + cross # 시계반대방향
        total_dist += min(calc_left, calc_right)
        
print(total_dist)