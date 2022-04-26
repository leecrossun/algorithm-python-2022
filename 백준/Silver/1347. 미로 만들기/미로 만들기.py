# 미로 만들기
N = int(input())
move = input()

size = (N * 2) + 1
maze = list(["#"] * size for _ in range(size))
x, y = size // 2, size // 2

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]
mv_idx = 2

maze[y][x] = "."

min_x, min_y = x, y
max_x, max_y = x, y

for m in move:
    if m == "R":
        mv_idx = (mv_idx + 1) % 4
    elif m == "L":
        mv_idx = (mv_idx + 3) % 4
    elif m == "F":
        x += mx[mv_idx]
        y += my[mv_idx]
        maze[y][x] = "."

        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

maze = maze[min_y : max_y + 1]
for line in maze:
    line = line[min_x : max_x + 1]
    for l in line:
        print(l, end='')
    print("")