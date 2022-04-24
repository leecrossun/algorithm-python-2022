# 종이자르기
weigh, height = map(int, input().split()) # 가로, 세로
count = int(input()) # 횟수
row = [0, height] # 가로로 자르기
col = [0, weigh] # 세로로 자르기

for _ in range(count):
    type, num = map(int, input().split())
    row.append(num) if type == 0 else col.append(num)

row.sort()
col.sort()

max_row, max_col = 0, 0
for i in range(len(row)-1):
    length = row[i+1] - row[i]
    max_row = length if length > max_row else max_row

for i in range(len(col)-1):
    length = col[i+1] - col[i]
    max_col = length if length > max_col else max_col

print(max_row * max_col)