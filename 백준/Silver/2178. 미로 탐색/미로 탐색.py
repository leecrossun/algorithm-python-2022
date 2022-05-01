# 미로 탐색
from copy import deepcopy
from collections import deque
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = deepcopy(maze)
r, c = 0, 0
N, M = N-1, M-1

# BFS
cnt = 1
q = deque([[r, c]])
visited[r][c] = 0
maze[r][c] = 1

mv_r = [0, 1, 0, -1]
mv_c = [1, 0, -1, 0]
while q:
    v = q.popleft()
    r, c = v[0], v[1]

    for i in range(4):
        to_r = r + mv_r[i]
        to_c = c + mv_c[i]
        if to_r >= 0 and to_r <= N and to_c >= 0 and to_c <= M and visited[to_r][to_c] == 1:
            q.append([to_r, to_c])
            visited[to_r][to_c] = 0
            maze[to_r][to_c] = maze[r][c] + 1

print(maze[N][M])