# 창고 다각형
N = int(input())
pillar = list(list(map(int, input().split())) for _ in range(N))
pillar.sort(key=lambda x:x[0])

max_height = max(pillar, key=lambda x:x[1])[1]
max_left, max_right = 0, 0
answer = 0

# 왼쪽
left = pillar[0][0]
left_h = pillar[0][1]
for i in range(N):
    l = pillar[i][0]
    h = pillar[i][1]

    if h > left_h:
        answer += (l - left) * left_h
        left, left_h = l, h

    if h == max_height:
        max_left = l
        break

# 오른쪽
right = pillar[N-1][0]
right_h = pillar[N-1][1]
for i in range(N-1, -1, -1):
    l = pillar[i][0]
    h = pillar[i][1]

    if h > right_h:
        answer += (right - l) * right_h
        right, right_h = l, h
    
    if h == max_height:
        max_right = l
        break

# 가장 높은 기둥
answer += (max_right - max_left + 1) * max_height
print(answer)    